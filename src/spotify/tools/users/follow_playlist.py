from src.spotify.tools.base import base_api_request

def follow_playlist() -> tuple[callable, dict]:
    def function(playlist_id: str, public: bool = None) -> str:
        route = f"/playlists/{playlist_id}/followers"
        
        body = {}
        if public is not None:
            body["public"] = public
        
        return base_api_request(route, "PUT", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_follow_playlist",
        "description": "Add the current user as a follower of a playlist.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "public": {
                    "type": "boolean",
                    "description": "Defaults to true. If true the playlist will be included in user's public playlists (added to profile), if false it will remain private."
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition
