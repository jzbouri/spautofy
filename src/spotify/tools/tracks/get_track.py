from src.spotify.tools.base import base_api_request

def get_track() -> tuple[callable, dict]:
    def function(id: str) -> str:
        route = f"/tracks/{id}"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_track",
        "description": "Get Spotify catalog information for a single track identified by its unique Spotify ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The Spotify ID for the track. Example: 11dFghVXANMlKmJXsNCbNl"
                }
            },
            "required": ["id"]
        }
    }
    
    return function, tool_definition
