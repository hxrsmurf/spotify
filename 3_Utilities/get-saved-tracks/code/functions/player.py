from email import header
import json
import requests
from .authorization import get_access_token

def get_saved_tracks():
    spotify_url = ' https://api.spotify.com/v1/me/tracks'
    headers = {
        'Authorization' : 'Bearer ' + str(get_access_token()),
        'Content-Type' : 'application/json'
    }
    offset = 0
    params = {'limit' : 50, 'offset': offset}

    response = requests.get(spotify_url, headers=headers, params=params)

    status_code = response.status_code

    if 'next' in response:
        print(response['next'])

    if not status_code == 200:
        print(f'Player Status Code {status_code}')
        print(f'Player Content: {response.content}')
    else:
        response_json = json.loads(response.content)
        return response_json