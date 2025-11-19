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
]

tools_dict = {}

for tool_function in tools_functions:
    function, tool_definition = tool_function()
    tools_dict[tool_definition["name"]] = {
        "function": function,
        "tool_definition": tool_definition
    }