from src.spotify.tools.base import base_api_request

def add_item_to_playback_queue() -> tuple[callable, dict]:
    def function(uri: str, device_id: str = None) -> str:
        route = f"/me/player/queue"
        
        params = {}
        params["uri"] = uri
        if device_id:
            params["device_id"] = device_id
            
        return base_api_request(route, "POST", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "add_item_to_playback_queue",
        "description": "Add an item to be played next in the user's current playback queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "uri": {
                    "type": "string",
                    "description": "The uri of the item to add to the queue. Must be a track or an episode uri. Example: spotify%3Atrack%3A4iV5W9uYEdYUVa79Axb7Rh"
                },
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": ["uri"]
        }
    }
    
    return function, tool_definition