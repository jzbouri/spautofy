from src.lastfm.tools.base import base_api_request

def get_top_tags() -> tuple[callable, dict]:
    def function(user: str, limit: int = None) -> str:
        
        params = {
            "method": "user.gettoptags",
            "user": user
        }
        
        if limit:
            params["limit"] = limit
            
        return base_api_request(method="GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "lastfm_get_top_tags",
        "description": "Get the top tags used by this user.",
        "parameters": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "string",
                    "description": "The user name."
                },
                "limit": {
                    "type": "integer",
                    "description": "Limit the number of tags returned."
                }
            },
            "required": ["user"]
        }
    }
    
    return function, tool_definition