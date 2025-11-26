from src.spotify.tools.base import base_api_request

def remove_users_saved_albums() -> tuple[callable, dict]:
    def function(ids: list[str]) -> str:
        route = f"/me/albums"
        
        body = {}
        body["ids"] = ids
        
        return base_api_request(route, "DELETE", body=body)
    
    tool_definition = {
        "type": "function",
        "name": "spotify_remove_users_saved_albums",
        "description": "Remove one or more albums from the current user's 'Your Music' library.",
        "parameters": {
            "type": "object",
            "properties": {
                "ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "An array of the Spotify IDs for the albums. Maximum: 20 IDs. Example: ['382ObEPsp2rxGrnsizN5TX', '1A2GTWGtFfWp7KSQTwWOyo', '2noRn2Aes5aoNVsU6iWThc']"
                }
            },
            "required": ["ids"]
        }
    }
    
    return function, tool_definition
