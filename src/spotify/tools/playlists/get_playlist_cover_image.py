from src.spotify.tools.base import base_api_request

def get_playlist_cover_image() -> tuple[callable, dict]:
    def function(playlist_id: str) -> str:
        route = f"/playlists/{playlist_id}/images"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "get_playlist_cover_image",
        "description": "Get the cover image for a playlist.",
    }
    
    return function, tool_definition