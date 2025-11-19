from src.spotify.tools.base import base_api_request

def search_for_item() -> tuple[callable, dict]:
    def function(q: str, type: list[str], limit: int = None, offset: int = None, include_external: str = None) -> str:
        route = f"/search"

        params = {}
        params["q"] = q
        params["type"] = type
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        if include_external:
            params["include_external"] = include_external
            
        return base_api_request(route, "GET", params=params)
    
    tool_definition = {
        "type": "function",
        "name": "search_for_item",
        "description": "Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that match a keyword string. Audiobooks are only available within the US, UK, Canada, Ireland, New Zealand and Australia markets.",
        "parameters": {
            "type": "object",
            "properties": {
                "q": {
                    "type": "string",
                    "description": "You can narrow down your search using field filters. The available filters are album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre. Each field filter only applies to certain result types. The artist and year filters can be used while searching albums, artists and tracks. You can filter on a single year or a range (e.g. 1955-1960). The album filter can be used while searching albums and tracks. The genre filter can be used while searching artists and tracks. The isrc and track filters can be used while searching tracks. The upc, tag:new and tag:hipster filters can only be used while searching albums. The tag:new filter will return albums released in the past two weeks and tag:hipster can be used to return only albums with the lowest 10% popularity. Example: remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davi"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "An array of item types to search across. Search results include hits from all the specified item types. For example: q=abacab&type=album,track returns both albums and tracks matching 'abacab'. Allowed values: 'album', 'artist', 'playlist', 'track', 'show', 'episode', 'audiobook'"
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of results to return in each item type. Default: 20. Range: 0 - 50. Example: 10"
                },
                "offset": {
                    "type": "integer",
                    "description": "The index of the first result to return. Use with limit to get the next page of search results. Default: 0. Range: 0 - 1000. Example: 5"
                },
                "include_external": {
                    "type": "string",
                    "description": "If include_external=audio is specified it signals that the client can play externally hosted audio content, and marks the content as playable in the response. By default externally hosted audio content is marked as unplayable in the response. Allowed values: 'audio'"
                }
            },
            "required": ["q", "type"]
        }
    }
    
    return function, tool_definition