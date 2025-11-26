from src.spotify.tools.base import base_api_request

def get_users_profile() -> tuple[callable, dict]:
    def function(user_id: str) -> str:
        route = f"/users/{user_id}"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_users_profile",
        "description": "Get public profile information about a Spotify user.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user's Spotify user ID. Example: smedjan"
                }
            },
            "required": ["user_id"]
        }
    }
    
    return function, tool_definition
