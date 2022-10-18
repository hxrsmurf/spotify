from functions.authorization import get_access_token
from functions.player import get_saved_tracks
from functions.utils import handle_saved_tracks, shuffle_tracks
from functions.playlist import create_playlist, create_shuffled_playlist

def handler(event, context):
    access_token = get_access_token()
    tracks = get_saved_tracks(access_token)
    shuffled_tracks = shuffle_tracks(handle_saved_tracks(tracks))
    create_shuffled_playlist(access_token=access_token, tracks=shuffled_tracks)