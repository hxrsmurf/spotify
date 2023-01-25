import json
import requests

from .dynamodb import put_item
from .utils import current_year_month_day

def create_playlist(access_token):
    spotify_url = 'https://api.spotify.com/v1/me/playlists'
    headers = {
        'Authorization' : 'Bearer ' + str(access_token),
        'Content-Type' : 'application/json'
    }
    params = {'limit' : 50}

    playlist_name = f'Shuffled Liked - {current_year_month_day()}'

    body = {
        'name': playlist_name,
        'description' : playlist_name
    }

    response = requests.post(spotify_url, headers=headers, json=body)

    status_code = response.status_code
    if not status_code == 201:
        print(f'Player Status Code {status_code}')
        print(f'Player Content: {response.content}')
    else:
        response_json = json.loads(response.content)
        put_item(playlist_information=response_json)
        return response_json['id']

def create_shuffled_playlist(access_token, tracks):
    playlist_id = create_playlist(access_token)
    spotify_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    headers = {
        'Authorization' : 'Bearer ' + str(access_token),
        'Content-Type' : 'application/json'
    }

    body = {
        'uris': tracks
    }

    response = requests.post(spotify_url, headers=headers, json=body)

    status_code = response.status_code
    if not status_code == 201:
        print(f'Player Status Code {status_code}')
        print(f'Player Content: {response.content}')
    else:
        response_json = json.loads(response.content)
        print(response_json)
        return playlist_id

# https://developer.spotify.com/documentation/general/guides/working-with-playlists/#following-and-unfollowing-a-playlist
def unfollow_playlist(access_token, playlist_id):
    spotify_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/followers'

    headers = {
        'Authorization' : 'Bearer ' + str(access_token),
        'Content-Type' : 'application/json'
    }

    response = requests.delete(spotify_url)
    # Getting 401 unauthorized even though the token is fine.
    print(response)

def check_user_follows_playlist(access_token, playlist_id):
    spotify_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/contains'

    headers = {
        'Authorization' : 'Bearer ' + str(access_token),
        'Content-Type' : 'application/json'
    }

    response = requests.get(spotify_url)
    print(response)