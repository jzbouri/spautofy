from src.spotify.tools.base import base_api_request

def update_playlist_items() -> tuple[callable, dict]:
    def function(playlist_id: str, uris: list[str] = None, range_start: int = None, insert_before: int = None, range_length: int = None, snapshot_id: str = None) -> str:
        route = f"/playlists/{playlist_id}/tracks"
        
        body = {}
        if uris:
            body["uris"] = uris
        if range_start:
            body["range_start"] = range_start
        if insert_before:
            body["insert_before"] = insert_before
        if range_length:
            body["range_length"] = range_length
        if snapshot_id:
            body["snapshot_id"] = snapshot_id
            
        return base_api_request(route, "PUT", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "update_playlist_items",
        "description": "Either reorder or replace items in a playlist depending on the request's parameters. To reorder items, include range_start, insert_before, range_length and snapshot_id in the request's body. To replace items, include uris as either a query parameter or in the request's body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist. Note: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can't be applied together in a single request.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "uris": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify track URIs to add. For example: {uris: ['spotify:track:4iV5W9uYEdYUVa79Axb7Rh', 'spotify:track:1301WleyT98MSxVHPZCA6M', 'spotify:episode:512ojhOuo1ktJprKbVcKyQ']} A maximum of 100 items can be set in one request."
                },
                "range_start": {
                    "type": "integer",
                    "description": "The position of the first item to be reordered."
                },
                "insert_before": {
                    "type": "integer",
                    "description": "The position where the items should be inserted. To reorder the items to the end of the playlist, simply set insert_before to the position after the last item. Examples: To reorder the first item to the last position in a playlist with 10 items, set range_start to 0, and insert_before to 10. To reorder the last item in a playlist with 10 items to the start of the playlist, set range_start to 9, and insert_before to 0."
                },
                "range_length": {
                    "type": "integer",
                    "description": "The amount of items to be reordered. Defaults to 1 if not set. The range of items to be reordered begins from the range_start position, and includes the range_length subsequent items. Example: To move the items at index 9-10 to the start of the playlist, range_start is set to 9, and range_length is set to 2."
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