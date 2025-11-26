from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import json
from typing import Generator

from src.db.db_manager import DatabaseManager
from src.llm.tools_master import tools_dict, tools_definitions

load_dotenv()

db_manager = DatabaseManager()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def _clean_llm_event(llm_event: dict) -> dict:
    if "status" in llm_event:
        llm_event.pop("status")
    return llm_event

def _get_new_events_from_llm(chat_id: str, events: list[dict]) -> list[dict]:
    while True:
        try:
            response = client.responses.create(
                model="gpt-5",
                tools=tools_definitions,
                input=events,
            )
            break
        except Exception as e:
            print(f"Error getting LLM response: {e}")
            time.sleep(60)
    
    db_manager.store_llm_response(
        chat_id=chat_id,
        input_tokens=response.usage.input_tokens,
        cached_tokens=response.usage.input_tokens_details.cached_tokens,
        output_tokens=response.usage.output_tokens,
    )

    return [_clean_llm_event(dict(item.model_dump())) for item in response.output]

def handle_user_message(chat_id: str, new_user_message: str) -> Generator[dict, None, None]:
    user_message_event_object = {
        "role": "user",
        "content": new_user_message
    }
    
    db_manager.store_chat_event(chat_id, 'user_message', user_message_event_object)
    
    yield user_message_event_object
    
    existing_event_objects = [event['event_object'] for event in db_manager.get_chat_events(chat_id)]
    new_event_objects = _get_new_events_from_llm(chat_id, existing_event_objects)
    all_event_objects = existing_event_objects + new_event_objects
    
    [db_manager.store_chat_event(
        chat_id=chat_id, 
        event_type=event_object['type'], 
        event_object=event_object) 
     for event_object in new_event_objects]

    for event_object in new_event_objects:
        yield event_object

    while True:
        function_calls_made = False
        
        for event_object in new_event_objects:
            if event_object['type'] == "function_call":
                function_calls_made = True
                arguments = json.loads(event_object['arguments'])

                function_name = tools_dict[event_object['name']]['function']
                function_response = function_name(**arguments)
                
                function_output_object = {
                    "type": "function_call_output",
                    "call_id": event_object['call_id'],
                    "output": function_response
                }
                
                yield function_output_object
                
                db_manager.store_chat_event(chat_id, 'function_call_output', function_output_object)
                all_event_objects.append(function_output_object)
    
        if not function_calls_made:
            break

        new_event_objects = _get_new_events_from_llm(chat_id, all_event_objects)
        all_event_objects.extend(new_event_objects)
        
        [db_manager.store_chat_event(
            chat_id=chat_id, 
            event_type=event_object['type'], 
            event_object=event_object) 
        for event_object in new_event_objects]
        
        for event_object in new_event_objects:
            yield event_object