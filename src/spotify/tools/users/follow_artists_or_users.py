from src.spotify.tools.base import base_api_request

def follow_artists_or_users() -> tuple[callable, dict]:
    def function(type: str, ids: list[str]) -> str:
        route = f"/me/following"
        
        params = {
            "type": type
        }
        
        body = {
            "ids": ids
        }
        
        return base_api_request(route, "PUT", params=params, body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_follow_artists_or_users",
        "description": "Add the current user as a follower of one or more artists or other Spotify users.",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "The ID type. Allowed values: 'artist', 'user'"
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
