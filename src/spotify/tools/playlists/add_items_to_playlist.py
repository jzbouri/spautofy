from src.spotify.tools.base import base_api_request

def add_items_to_playlist() -> tuple[callable, dict]:
    def function(playlist_id: str, position: int = None, uris: list[str] = None) -> str:
        route = f"/playlists/{playlist_id}/tracks"
        
        body = {}
        if position:
            body["position"] = position
        if uris:
            body["uris"] = uris
        
        return base_api_request(route, "POST", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "add_items_to_playlist",
        "description": "Add one or more items to a user's playlist.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "position": {
                    "type": "integer",
                    "description": "The position to insert the items, a zero-based index. For example, to insert the items in the first position: position=0; to insert the items in the third position: position=2. If omitted, the items will be appended to the playlist. Items are added in the order they are listed in the query string or request body. Example: 0"
                },
                "uris": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "An array of Spotify URIs to add, can be track or episode URIs. For example: {uris: ['spotify:track:4iV5W9uYEdYUVa79Axb7Rh', 'spotify:track:1301WleyT98MSxVHPZCA6M', 'spotify:episode:512ojhOuo1ktJprKbVcKyQ']} A maximum of 100 items can be added in one request."
                }
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition