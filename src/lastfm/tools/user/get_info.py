from src.lastfm.tools.base import base_api_request

def get_info() -> tuple[callable, dict]:
    def function(user: str) -> str:
        
        params = {
            "method": "user.getinfo",
            "user": user
        }
        
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_user_info",
        "description": "Get information about a user profile on Last.fm.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The user to fetch info for."
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition