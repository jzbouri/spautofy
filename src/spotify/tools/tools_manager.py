from src.spotify.tools.albums.check_users_saved_albums import check_users_saved_albums
from src.spotify.tools.albums.get_album_tracks import get_album_tracks
from src.spotify.tools.albums.get_album import get_album
from src.spotify.tools.albums.get_new_releases import get_new_releases
from src.spotify.tools.albums.get_several_albums import get_several_albums
from src.spotify.tools.albums.get_users_saved_albums import get_users_saved_albums
from src.spotify.tools.albums.remove_users_saved_albums import remove_users_saved_albums
from src.spotify.tools.albums.save_albums_for_current_user import save_albums_for_current_user

from src.spotify.tools.player.add_item_to_playback_queue import add_item_to_playback_queue
from src.spotify.tools.player.get_available_devices import get_available_devices
from src.spotify.tools.player.get_currently_playing_track import get_currently_playing_track
from src.spotify.tools.player.get_playback_state import get_playback_state
from src.spotify.tools.player.get_recently_played_tracks import get_recently_played_tracks
from src.spotify.tools.player.get_user_queue import get_user_queue
from src.spotify.tools.player.pause_playback import pause_playback
from src.spotify.tools.player.seek_to_position import seek_to_position
from src.spotify.tools.player.set_playback_volume import set_playback_volume
from src.spotify.tools.player.set_repeat_mode import set_repeat_mode
from src.spotify.tools.player.skip_to_next import skip_to_next
from src.spotify.tools.player.skip_to_previous import skip_to_previous
from src.spotify.tools.player.start_or_resume_playback import start_or_resume_playback
from src.spotify.tools.player.toggle_playback_shuffle import toggle_playback_shuffle
from src.spotify.tools.player.transfer_playback import transfer_playback

from src.spotify.tools.search.search_for_item import search_for_item

from src.spotify.tools.playlists.get_playlist import get_playlist
from src.spotify.tools.playlists.change_playlist_details import change_playlist_details
from src.spotify.tools.playlists.get_playlist_items import get_playlist_items
from src.spotify.tools.playlists.update_playlist_items import update_playlist_items
from src.spotify.tools.playlists.add_items_to_playlist import add_items_to_playlist
from src.spotify.tools.playlists.remove_playlist_items import remove_playlist_items
from src.spotify.tools.playlists.get_current_users_playlists import get_current_users_playlists
from src.spotify.tools.playlists.get_users_playlists import get_users_playlists
from src.spotify.tools.playlists.create_playlist import create_playlist
from src.spotify.tools.playlists.get_playlist_cover_image import get_playlist_cover_image
from src.spotify.tools.playlists.add_custom_playlist_cover_image import add_custom_playlist_cover_image

from src.spotify.tools.users.get_current_users_profile import get_current_users_profile
from src.spotify.tools.users.get_current_users_top_items import get_current_users_top_items
from src.spotify.tools.users.get_users_profile import get_users_profile
from src.spotify.tools.users.follow_playlist import follow_playlist
from src.spotify.tools.users.unfollow_playlist import unfollow_playlist
from src.spotify.tools.users.get_followed_artists import get_followed_artists
from src.spotify.tools.users.follow_artists_or_users import follow_artists_or_users
from src.spotify.tools.users.unfollow_artists_or_users import unfollow_artists_or_users
from src.spotify.tools.users.check_if_user_follows_artists_or_users import check_if_user_follows_artists_or_users
from src.spotify.tools.users.check_if_current_user_follows_playlist import check_if_current_user_follows_playlist

from src.spotify.tools.tracks.get_track import get_track
from src.spotify.tools.tracks.get_several_tracks import get_several_tracks
from src.spotify.tools.tracks.get_users_saved_tracks import get_users_saved_tracks
from src.spotify.tools.tracks.save_tracks_for_current_user import save_tracks_for_current_user
from src.spotify.tools.tracks.remove_users_saved_tracks import remove_users_saved_tracks
from src.spotify.tools.tracks.check_users_saved_tracks import check_users_saved_tracks

tools_functions = [
    check_users_saved_albums,
    get_album,
    get_album_tracks,
    # get_new_releases, (Appears deprecated)
    get_several_albums,
    get_users_saved_albums,
    remove_users_saved_albums,
    save_albums_for_current_user,
    add_item_to_playback_queue,
    get_available_devices,
    get_currently_playing_track,
    get_playback_state,
    get_recently_played_tracks,
    get_user_queue,
    pause_playback,
    seek_to_position,
    set_playback_volume,
    set_repeat_mode,
    skip_to_next,
    skip_to_previous,
    start_or_resume_playback,
    toggle_playback_shuffle,
    transfer_playback,
    search_for_item,
    get_playlist,
    change_playlist_details,
    get_playlist_items,
    update_playlist_items,
    add_items_to_playlist,
    remove_playlist_items,
    get_current_users_playlists,
    get_users_playlists,
    create_playlist,
    get_playlist_cover_image,
    add_custom_playlist_cover_image,
    get_current_users_profile,
    get_current_users_top_items,
    get_users_profile,
    follow_playlist,
    unfollow_playlist,
    get_followed_artists,
    follow_artists_or_users,
    unfollow_artists_or_users,
    check_if_user_follows_artists_or_users,
    check_if_current_user_follows_playlist,
    get_track,
    get_several_tracks,
    get_users_saved_tracks,
    save_tracks_for_current_user,
    remove_users_saved_tracks,
    check_users_saved_tracks,
]

tools_dict = {}

for tool_function in tools_functions:
    function, tool_definition = tool_function()
    tools_dict[tool_definition["name"]] = {
        "function": function,
        "tool_definition": tool_definition
    }