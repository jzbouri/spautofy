from src.spotify.tools.base import base_api_request

def set_playback_volume() -> tuple[callable, dict]:
    def function(volume_percent: int, device_id: str = None) -> str:
        route = f"/me/player/volume"
        
        params = {
            "volume_percent": volume_percent
        }
        if device_id:
            params["device_id"] = device_id
            
        return base_api_request(route, "PUT", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_set_playback_volume",
        "description": "Set the volume for the user's current playback device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "volume_percent": {
                    "type": "integer",
                    "description": "The volume to set. Must be a value from 0 to 100 inclusive. Example: 50"
                },
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": ["volume_percent"]
        }
    }
    
    return function, tool_definition
