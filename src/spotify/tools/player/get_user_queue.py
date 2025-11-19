from src.spotify.tools.base import base_api_request

def get_user_queue() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me/player/queue"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_user_queue",
        "description": "Get the list of objects that make up the user's queue.",
    }
    
    return function, tool_definition