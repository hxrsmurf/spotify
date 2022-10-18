import json
import requests

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
        return response_json['id']