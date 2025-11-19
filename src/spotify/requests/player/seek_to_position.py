from src.spotify.requests.base_request import base_request

def seek_to_position() -> tuple[callable, dict]:
    def function(position_ms: int, device_id: str = None) -> str:
        route = f"/me/player/seek"
        
        params = {}
        params["position_ms"] = position_ms
        if device_id:
            params["device_id"] = device_id
            
        return base_request(route, "PUT", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "seek_to_position",
        "description": "Seeks to the given position in the user's currently playing track. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "position_ms": {
                    "type": "integer",
                    "description": "The position in milliseconds to seek to. Must be a positive number. Passing in a position that is greater than the length of the track will cause the player to start playing the next song. Example: 25000"
                },
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": ["position_ms"]
        }
    }
    
    return function, tool_definition