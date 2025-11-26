from src.spotify.tools.base import base_api_request

def get_playlist() -> tuple[callable, dict]:
    def function(playlist_id: str, fields: list[str] = None) -> str:
        route = f"/playlists/{playlist_id}"
        
        params = {}
        if fields:
            params["fields"] = fields
        
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_get_playlist",
        "description": "Get a playlist owned by a Spotify user.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "string",
                    "description": "The Spotify ID of the playlist. Example: 3cEYpjA9oz9GiPac4AsH4n"
                },
                "fields": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Filters for the query: an array of the fields to return. If omitted, all fields are returned. For example, to get just the playlist's description and URI: description,uri. A dot separator can be used to specify non-reoccurring fields, while parentheses can be used to specify reoccurring fields within objects. For example, to get just the added date and user ID of the adder: tracks.items(added_at,added_by.id). Use multiple parentheses to drill down into nested objects, for example: tracks.items(track(name,href,album(name,href))). Fields can be excluded by prefixing them with an exclamation mark, for example: tracks.items(track(name,href,album(!name,href))) Example: items(added_by.id,track(name,href,album(name,href)))"
                },
            },
            "required": ["playlist_id"]
        }
    }
    
    return function, tool_definition
