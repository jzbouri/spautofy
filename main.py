from src.db.db_manager import DatabaseManager
import questionary
import sys
import os
from rich import print
from rich.text import Text

from src.llm.response import handle_user_message
from src.llm.output import get_output_text, DASH_COUNT

db_manager = DatabaseManager()

def _print_separator():
    separator = Text("-" * DASH_COUNT, style="dim")
    print(separator)

def _clear_previous_line():
    sys.stdout.write("\033[A\033[2K")
    sys.stdout.flush()

def _clear_separator_and_input():
    sys.stdout.write("\033[A\033[2K\033[A\033[2K")
    sys.stdout.flush()
    
def _clear_screen():
    os.system('clear')  
    
_clear_screen()

while True:
    chats = db_manager.get_all_chats()

    if chats:
        chat_index = questionary.select(
            "Select one of the following chats using the arrow keys. Press Enter to confirm your selection.",
            choices=[f"{i}: {chat['created_at'].strftime('%Y-%m-%d %H:%M:%S')}" for i, chat in enumerate(chats)] + ["Create new chat"]
        ).ask()
        if chat_index == "Create new chat":
            chat_id = db_manager.store_chat()['id']
        else:
            chat_id = chats[int(chat_index.split(":")[0])]['id']
    else:
        chat_id = db_manager.store_chat()['id']

    events = [event for event in db_manager.get_chat_events(chat_id)]
    
    _clear_screen()

    for event in events:
        print(get_output_text(event['event_object']))

    while True:
        _print_separator()
        user_input = input("You (q=quit, s=switch) - ").strip()
        
        if not user_input:
            _clear_previous_line()
            continue

        if user_input.lower() == 'q':
            _clear_separator_and_input()
            sys.exit(0)
        
        if user_input.lower() == 's':
            _clear_separator_and_input()
            _clear_screen()
            break

        _clear_separator_and_input()

        for event_object in handle_user_message(chat_id, user_input):
            print(get_output_text(event_object))
