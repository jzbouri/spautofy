from src.spotify.requests.base_request import base_request

def transfer_playback() -> tuple[callable, dict]:
    def function(device_ids: list[str], play: bool = None) -> str:
        route = f"/me/player"
        
        body = {}
        body["device_ids"] = device_ids
        if play:
            body["play"] = play
        
        return base_request(route, "PUT", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "transfer_playback",
        "description": "Transfer playback to a new device and optionally begin playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.",
        "parameters": {
            "type": "object",
            "properties": {
                "device_ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A JSON array containing the ID of the device on which playback should be started/transferred. For example:{device_ids:['74ASZWbe4lXaubB36ztrGX']}. Note: Although an array is accepted, only a single device_id is currently supported. Supplying more than one will return 400 Bad Request"
                },
                "play": {
                    "type": "boolean",
                    "description": "true: ensure playback happens on new device. false or not provided: keep the current playback state."
                }
            },
            "required": ["device_ids"]
        }
    }
    
    return function, tool_definition