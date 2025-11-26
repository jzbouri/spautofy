from src.spotify.tools.base import base_api_request

def remove_users_saved_tracks() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/me/tracks"
        
        body = {
            "ids": ids
        }
        
        return base_api_request(route, "DELETE", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_remove_users_saved_tracks",
        "description": "Remove one or more tracks from the current user's 'Your Music' library.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify IDs. For example: ['4iV5W9uYEdYUVa79Axb7Rh', '1301WleyT98MSxVHPZCA6M']. A maximum of 50 items can be specified in one request."
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition
