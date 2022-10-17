from email import header
import json
import requests
from .authorization import get_access_token

def get_recently_played_tracks():
    spotify_url = 'https://api.spotify.com/v1/me/player/recently-played'
    headers = {
        'Authorization' : 'Bearer ' + str(get_access_token()),
        'Content-Type' : 'application/json'
    }

    response = requests.get(spotify_url, headers=headers)

    status_code = response.status_code

    if not status_code == 200:
        print(f'Player Status Code {status_code}')
        print(f'Player Content: {response.content}')
    else:
        response_json = json.loads(response.content)
        return response_json

def get_top_items(type, access_token, time_range):
    spotify_url = f'https://api.spotify.com/v1/me/top/{type}'
    headers = {
        'Authorization' : 'Bearer ' + access_token,
        'Content-Type' : 'application/json'
    }
    params = {'time_range' : time_range}

    response = requests.get(spotify_url, headers=headers, params=params)

    status_code = response.status_code
    if not status_code == 200:
        print(f'Status Code: {status_code}')
        return False
    else:
        return json.loads(response.content)