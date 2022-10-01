import requests
from requests.auth import HTTPBasicAuth
import json
import functions.ssm as ssm

# This gets the URL the user has to input and returns a code.
def get_authorization(client_id, redirect_uri):
    baseSpotifyURL = 'https://accounts.spotify.com/authorize?'
    response_type = "response_type=code"

    scope = 'scope=' + 'user-read-private user-read-email playlist-read-private user-top-read playlist-modify-public user-read-currently-playing user-read-recently-played playlist-read-collaborative playlist-modify-private user-read-playback-position user-library-read user-follow-read user-follow-modify user-modify-playback-state user-read-playback-state'
    state = 'state=state'

    client_id_string = 'client_id=' + client_id
    redirect_string = 'redirect_uri=' + redirect_uri

    spotifyURL = baseSpotifyURL + response_type + '&' + client_id_string + '&' + scope + '&' + redirect_string + '&' + state

    return(spotifyURL)


# This accepts the user's code and gives an access token and refresh token.
def get_access_token(code):
    baseSpotifyURL = 'https://accounts.spotify.com/api/token'

    basic = HTTPBasicAuth(client_id, client_secret)

    data = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    result = requests.post(baseSpotifyURL, auth=basic, data=data)
    print(result.content)
    # get_refresh_token - need to get a new refresh token and update a parameter.

# This accepts a refresh token and gives another access token and refresh token (if available).
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
def get_refresh_token(refresh_token, client_id, client_secret, refresh_token_parameter):
    baseSpotifyURL = 'https://accounts.spotify.com/api/token'
    basic = HTTPBasicAuth(client_id, client_secret)

    data = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    result = requests.post(baseSpotifyURL, auth=basic, data=data)
    result = json.loads(result.content)

    access_token = result['access_token']
    token_type = result['token_type']

    try:
        refresh_token = result['refresh_token']
        ssm.put(refresh_token_parameter, refresh_token)
    except:
        refresh_token = refresh_token

    result = {
        'access_token' : access_token,
        'refresh_token' : refresh_token,
        'token_type': token_type
    }

    return(result)