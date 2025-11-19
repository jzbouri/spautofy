from src.spotify.requests.base_request import base_request

def pause_playback() -> tuple[callable, dict]:
    def function(device_id: str = None) -> str:
        route = f"/me/player/pause"
        
        params = {}
        if device_id:
            params["device_id"] = device_id
        
        return base_request(route, "PUT", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "pause_playback",
        "description": "Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {
                    "type": "string",
                    "description": "The id of the device this command is targeting. If not supplied, the user's currently active device is the target. Example: 0d1841b0976bae2a3a310dd74c0f3df354899bc8"
                }
            },
            "required": []
        }
    }
    
    return function, tool_definition