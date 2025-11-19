from src.spotify.tools.base import base_api_request

def change_playlist_details() -> tuple[callable, dict]:
    def function(playlist_id: str, name: str = None, public: bool = None, collaborative: bool = None, description: str = None) -> str:
        route = f"/playlists/{playlist_id}"
        
        body = {}
        if name:
            body["name"] = name
        if public is not None:
            body["public"] = public
        if description:
            body["description"] = description
        if collaborative is not None:
            body["collaborative"] = collaborative

        return base_api_request(route, "PUT", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "change_playlist_details",
        "description": "Change a playlist's name and public/private state. (The user must, of course, own the playlist.)",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "name": {
                    "type": "string",
                    "description": "The new name for the playlist, for example 'My New Playlist Title'"
                },
                "public": {
                    "type": "boolean",
                    "description": "The playlist's public/private status (if it should be added to the user's profile or not): true the playlist will be public, false the playlist will be private, null the playlist status is not relevant."
                },
                "collaborative": {
                    "type": "boolean",
                    "description": "If true, the playlist will become collaborative and other users will be able to modify the playlist in their Spotify client. Note: You can only set collaborative to true on non-public playlists."
                },
                "description": {
                    "type": "string",
                    "description": "Value for playlist description as displayed in Spotify Clients and in the Web API."
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition