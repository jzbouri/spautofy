from src.spotify.tools.base import base_api_request

def get_several_artists() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/artists"
        
        params = {
            "ids": ids
        }
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_several_artists",
        "description": "Get Spotify catalog information for several artists based on their Spotify IDs.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify IDs for the artists. Maximum: 50 IDs. Example: ['2CIMQHirSU0MQqyYHq0eOx', '57dN52uHvrHOxijzpIgu3E', '1vCWHaC5f2uS3yhpwWbIA6']"
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition
