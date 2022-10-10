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