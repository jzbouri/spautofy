from src.spotify.tools.base import base_api_request

def get_artists_top_tracks() -> tuple[callable, dict]:
    def function(id: str) -> str:
        route = f"/artists/{id}/top-tracks"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_artists_top_tracks",
        "description": "Get Spotify catalog information about an artist's top tracks by country.",
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
