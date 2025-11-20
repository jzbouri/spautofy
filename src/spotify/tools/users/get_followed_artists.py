from src.spotify.tools.base import base_api_request

def get_followed_artists() -> tuple[callable, dict]:
    def function(type: str, after: str = None, limit: int = None) -> str:
        route = f"/me/following"
        
        params = {}
        params["type"] = type
        if after:
            params["after"] = after
        if limit:
            params["limit"] = limit
            
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "get_followed_artists",
        "description": "Get the current user's followed artists.",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "The ID type: currently only 'artist' is supported. Allowed values: 'artist'"
                },
                "after": {
                    "type": "string",
                    "description": "The last artist ID retrieved from the previous request. Example: 0I2XqVXqHScXjHhk6AYYRe"
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50. Example: 10"
                }
            },
            "required": ["type"]
        }
    }
    
    return function, tool_definition