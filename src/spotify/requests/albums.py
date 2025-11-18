from src.spotify.requests.base_request import base_request

def get_album(id: str, market: str = None):
    route = f"/albums/{id}"

    params = {}
    if market is not None:
        params["market"] = market
    
    return base_request(route, "GET", params=params)

def get_several_albums(ids: list[str], market: str = None):
    route = f"/albums"
    
    params = {}
    params["ids"] = ids
    if market is not None:
        params["market"] = market
    
    return base_request(route, "GET", params=params)

def get_album_tracks(id: str, market: str = None, limit: int = None, offset: int = None):
    route = f"/albums/{id}/tracks"
    
    params = {}
    if market is not None:
        params["market"] = market
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    
    return base_request(route, "GET", params=params)

def get_users_saved_albums(limit: int = None, offset: int = None, market: str = None):
    route = f"/me/albums"
    
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if market is not None:
        params["market"] = market
    
    return base_request(route, "GET", params=params)

def save_albums_for_current_user(ids: list[str]):
    route = f"/me/albums"
    
    body = {}
    body["ids"] = ids
    
    return base_request(route, "PUT", body=body)

def remove_users_saved_albums(ids: list[str]):
    route = f"/me/albums"
    
    body = {}
    body["ids"] = ids
    
    return base_request(route, "DELETE", body=body)

def check_users_saved_albums(ids: list[str]):
    route = f"/me/albums/contains"
    
    params = {}
    params["ids"] = ids
    
    return base_request(route, "GET", params=params)

def get_new_releases(limit: int = None, offset: int = None):
    route = f"/browse/new-releases"
    
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    
    return base_request(route, "GET", params=params)
