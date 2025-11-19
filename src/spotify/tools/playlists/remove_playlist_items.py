from src.spotify.tools.base import base_api_request

def remove_playlist_items() -> tuple[callable, dict]:
    def function(playlist_id: str, tracks: list[dict] = None, snapshot_id: str = None) -> str:
        route = f"/playlists/{playlist_id}/tracks"
        
        body = {}
        if tracks:
            body["tracks"] = tracks
        if snapshot_id:
            body["snapshot_id"] = snapshot_id
        
        return base_api_request(route, "DELETE", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "remove_playlist_items",
        "description": "Remove one or more items from a user's playlist.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "tracks": {
                    "type": "array",
                    "description": "An array of objects containing Spotify URIs of the tracks or episodes to remove. For example: { tracks: [{ uri: 'spotify:track:4iV5W9uYEdYUVa79Axb7Rh' },{ uri: 'spotify:track:1301WleyT98MSxVHPZCA6M' }] }. A maximum of 100 objects can be sent at once.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "uri": {
                                "type": "string",
                                "description": "Spotify URI"
                            }
                        }
                    }
                },
                "snapshot_id": {
                    "type": "string",
                    "description": "The playlist's snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist."
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition