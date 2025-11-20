from src.spotify.tools.base import base_api_request

def get_current_users_profile() -> tuple[callable, dict]:
    def function() -> str:
        route = f"/me"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_current_users_profile",
        "description": "Get detailed profile information about the current user (including the current user's username).",
    }
    
    return function, tool_definition