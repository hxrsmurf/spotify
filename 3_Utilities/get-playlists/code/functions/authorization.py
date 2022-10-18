import os
import json
import requests

from requests.auth import HTTPBasicAuth
from .ssm import get_parameter, put_parameter

def get_access_token():
    client_id = get_parameter(os.environ['SpotifyClientID'])
    client_secret = get_parameter(os.environ['SpotifyClientSecret'])
    ssm_refresh_token = get_parameter(os.environ['SpotifyRefreshToken'])

    spotify_token_url = 'https://accounts.spotify.com/api/token'
    basic_auth = HTTPBasicAuth(client_id, client_secret)

    data = {
        'refresh_token' : ssm_refresh_token,
        'grant_type' : 'refresh_token'
    }

    response = requests.post(spotify_token_url, auth=basic_auth, data=data)
    response_json = json.loads(response.content)
    access_token = response_json['access_token']

    if 'refresh_token' in response_json:
        refresh_token = response_json['refresh_token']
        if not ssm_refresh_token == refresh_token:
            print(f'Updating Refresh Token')
            put_parameter(refresh_token)

    return access_token

