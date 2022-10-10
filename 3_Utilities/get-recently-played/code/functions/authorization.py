import os
import json
import requests

from requests.auth import HTTPBasicAuth
from .ssm import get_parameter, put_parameter

def get_access_token():
    client_id = get_parameter(os.environ['SpotifyClientID'])
    client_secret = get_parameter(os.environ['SpotifyClientSecret'])
    refresh_token = get_parameter(os.environ['SpotifyRefreshToken'])

    spotify_token_url = 'https://accounts.spotify.com/api/token'
    basic_auth = HTTPBasicAuth(client_id, client_secret)

    data = {
        'refresh_token' : refresh_token,
        'grant_type' : 'refresh_token'
    }

    response = requests.post(spotify_token_url, auth=basic_auth, data=data)
    response_json = json.loads(response.content)

    # If new Refresh Token, update SSM
    try:
        print(f'Updating Refresh Token')
        refresh_token = response_json['refresh_token']
        put_parameter(refresh_token)
    except:
        pass

    return response_json['access_token']