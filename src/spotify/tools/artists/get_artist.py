from src.spotify.tools.base import base_api_request

def get_artist() -> tuple[callable, dict]:
    def function(id: str) -> str:
        route = f"/artists/{id}"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_artist",
        "description": "Get Spotify catalog information for a single artist identified by their unique Spotify ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The Spotify ID of the artist. Example: 0TnOYISbd1XYRBk9myaseg"
                }
            },
            "required": ["id"]
        }
    }
    
    return function, tool_definition