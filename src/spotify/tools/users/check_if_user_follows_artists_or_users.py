from src.spotify.tools.base import base_api_request

def check_if_user_follows_artists_or_users() -> tuple[callable, dict]:
    def function(type: str, ids: list[str]) -> str:
        route = f"/me/following/contains"
        
        params = {}
        params["type"] = type
        params["ids"] = ids
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "check_if_user_follows_artists_or_users",
        "description": "Check to see if the current user is following one or more artists or other Spotify users.",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "The ID type: either 'artist' or 'user'. Allowed values: 'artist', 'user'"
                },
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the artist or user Spotify IDs. For example: ['74ASZWbe4lXaubB36ztrGX', '08td7MxkoHQkXnWAYD8d6Q']. A maximum of 50 IDs can be sent in one request."
                }
            },
            "required": ["type", "ids"]
        }
    }
    
    return function, tool_definition