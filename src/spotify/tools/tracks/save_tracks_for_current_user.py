from src.spotify.tools.base import base_api_request

def save_tracks_for_current_user() -> tuple[callable, dict]:
    def function(ids: list[str] = None, timestamped_ids: list[dict] = None) -> str:
        route = f"/me/tracks"
        
        body = {}
        if timestamped_ids:
            body["timestamped_ids"] = timestamped_ids
        elif ids:
            body["ids"] = ids
        
        return base_api_request(route, "PUT", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_save_tracks_for_current_user",
        "description": "Save one or more tracks to the current user's 'Your Music' library. At least one of 'ids' or 'timestamped_ids' must be provided.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array of the Spotify IDs. For example: ['4iV5W9uYEdYUVa79Axb7Rh', '1301WleyT98MSxVHPZCA6M']. A maximum of 50 items can be specified in one request. Note: if timestamped_ids is present, any IDs listed here will be ignored."
                },
                "timestamped_ids": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "The Spotify ID for the track."
                            },
                            "added_at": {
                                "type": "string",
                                "description": "The timestamp when the track was added to the library. Use ISO 8601 format with UTC timezone (e.g., '2023-01-15T14:30:00Z'). You can specify past timestamps to insert tracks at specific positions in the library's chronological order. The API uses minute-level granularity for ordering, though the timestamp supports millisecond precision."
                            }
                        },
                        "required": ["id", "added_at"]
                    },
                    "description": "A JSON array of objects containing track IDs with their corresponding timestamps. Each object must include a track ID and an added_at timestamp. A maximum of 50 items can be specified in one request. Note: if this is present, any IDs listed in the ids field will be ignored."
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition
