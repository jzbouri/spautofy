from src.spotify.tools.base import base_api_request

def check_users_saved_tracks() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/me/tracks/contains"
        
        params = {
            "ids": ids
        }
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_check_users_saved_tracks",
        "description": "Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify IDs. For example: ['4iV5W9uYEdYUVa79Axb7Rh', '1301WleyT98MSxVHPZCA6M']. Maximum: 50 IDs."
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition
