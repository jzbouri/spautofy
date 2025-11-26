from src.spotify.tools.base import base_api_request

def get_several_tracks() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/tracks"
        
        params = {
            "ids": ids
        }
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_several_tracks",
        "description": "Get Spotify catalog information for multiple tracks based on their Spotify IDs.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify IDs for the tracks. Maximum: 50 IDs. Example: ['4iV5W9uYEdYUVa79Axb7Rh', '1301WleyT98MSxVHPZCA6M']"
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition
