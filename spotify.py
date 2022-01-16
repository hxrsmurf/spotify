import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime

client_id = ''
client_secret = ''
redirect_uri = ''

client_id_string = 'client_id=' + client_id
redirect_string = 'redirect_uri=' + redirect_uri

dt = datetime.now()
# Set timestamp as 2022-01-10 18:59:00:00
timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')

# This gets the URL the user has to input and returns a code.
def getAuthorization():
    baseSpotifyURL = 'https://accounts.spotify.com/authorize?'
    response_type = "response_type=code"
    
    scope = 'scope=' + 'user-read-private user-read-email playlist-read-private user-top-read playlist-modify-public user-read-currently-playing user-read-recently-played playlist-read-collaborative playlist-modify-private user-read-playback-position user-library-read user-follow-read user-follow-modify user-modify-playback-state user-read-playback-state'
    state = 'state=state'

    spotifyURL = baseSpotifyURL + response_type + '&' + client_id_string + '&' + scope + '&' + redirect_string + '&' + state

    print(spotifyURL)

# This accepts the user's code and gives an access token and refresh token.
def getAccessToken(code):
    baseSpotifyURL = 'https://accounts.spotify.com/api/token'

    basic = HTTPBasicAuth(client_id, client_secret)

    data = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    result = requests.post(baseSpotifyURL, auth=basic, data=data)
    print(result.content)

# This accepts a refresh token and gives another access token and refresh token (if available).
def getRefreshToken(refresh_token):
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
    except:
        refresh_token = refresh_token
        #print('No refresh token')
        pass

    result = {
        'access_token' : access_token,
        'refresh_token' : refresh_token,
        'token_type': token_type
    }
    
    return(result)

def getPlayer(access_token):
    spotifyUrl =  'https://api.spotify.com/v1/me/player'    
    headers = {"Authorization": "Bearer " + str(access_token)}
    result = requests.get(spotifyUrl, headers=headers)
    result = json.loads(result.content)
    
    result = {
        'songID': result['item']['id'],
        'song' : result['item']['name'],
        'artist' : result['item']['artists'][0]['name']
    }
    print(result)

# getAuthorization()

code = ''
# getAccessToken(code)

refresh_token = ''
access_token = getRefreshToken(refresh_token)['access_token']
getPlayer(access_token)