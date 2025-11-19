from src.spotify.tools.base import base_api_request

def create_playlist() -> tuple[callable, dict]:
    def function(user_id: str, name: str, public: bool = None, collaborative: bool = None, description: str = None) -> str:
        route = f"/users/{user_id}/playlists"
        
        body = {}
        body["name"] = name
        if public is not None:
            body["public"] = public
        if collaborative is not None:
            body["collaborative"] = collaborative
        if description:
            body["description"] = description
            
        return base_api_request(route, "POST", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "create_playlist",
        "description": "Create a playlist for a Spotify user. (The playlist will be empty until you add tracks.) Each user is generally limited to a maximum of 11000 playlists.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user's Spotify user ID. Example: smedjan"
                },
                "name": {
                    "type": "string",
                    "description": "The name for the new playlist, for example 'Your Coolest Playlist'. This name does not need to be unique; a user may have several playlists with the same name."
                },
                "public": {
                    "type": "boolean",
                    "description": "Defaults to true. The playlist's public/private status (if it should be added to the user's profile or not): true the playlist will be public, false the playlist will be private."
                },
                "collaborative": {
                    "type": "boolean",
                    "description": "Defaults to false. If true the playlist will be collaborative. Note: to create a collaborative playlist you must also set public to false."
                },
                "description": {
                    "type": "string",
                    "description": "Value for playlist description as displayed in Spotify Clients and in the Web API."
                }
            },
            "required": ["user_id", "name"]
        }
    }
    
    return function, tool_definition