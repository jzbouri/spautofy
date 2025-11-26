from src.spotify.tools.base import base_api_request

def add_custom_playlist_cover_image() -> tuple[callable, dict]:
    def function(playlist_id: str, image_base64: str = None) -> str:
        route = f"/playlists/{playlist_id}/images"
        
        body = None
        if image_base64:
            body = image_base64
            
        content_type = "image/jpeg"
        
        return base_api_request(route, "PUT", body=body, content_type=content_type)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_add_custom_playlist_cover_image",
        "description": "Add a custom cover image to a playlist.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "image_base64": {
                    "type": "string",
                    "description": "Base64 encoded JPEG image data, maximum payload size is 256 KB. Example: '/9j/2wCEABoZGSccJz4lJT5CLy8vQkc9Ozs9R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0cBHCcnMyYzPSYmPUc9Mj1HR0dEREdHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR//dAAQAAf/uAA5BZG9iZQBkwAAAAAH/wAARCAABAAEDACIAAREBAhEB/8QASwABAQAAAAAAAAAAAAAAAAAAAAYBAQAAAAAAAAAAAAAAAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAARAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwAAARECEQA/AJgAH//Z'"
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition
