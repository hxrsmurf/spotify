from functions.authorization import get_access_token
from functions.player import get_playlists
from functions.utils import handle_playlist

def handler(event, context):
    access_token = get_access_token()
    playlists = get_playlists()
    results = handle_playlist(playlists)

    for playlist in results:
        print(playlist['name'], playlist['id'])