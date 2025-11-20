from src.spotify.tools.base import base_api_request

def check_if_current_user_follows_playlist() -> tuple[callable, dict]:
    def function(playlist_id: str) -> str:
        route = f"/playlists/{playlist_id}/followers/contains"
        
        return base_api_request(route, "GET")
    
    tool_definition = {
        "type": "function",
        "name": "check_if_current_user_follows_playlist",
        "description": "Check to see if the current user is following a specified playlist.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition