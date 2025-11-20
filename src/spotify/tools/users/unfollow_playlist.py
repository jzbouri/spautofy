from src.spotify.tools.base import base_api_request

def unfollow_playlist() -> tuple[callable, dict]:
    def function(playlist_id: str) -> str:
        route = f"/playlists/{playlist_id}/followers"
        
        return base_api_request(route, "DELETE")
    
    tool_definition = {
        "type": "function",
        "name": "unfollow_playlist",
        "description": "Remove the current user as a follower of a playlist.",
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