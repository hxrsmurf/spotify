import requests
from requests.auth import HTTPBasicAuth
import json
import functions.notify as notify

# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-information-about-the-users-current-playback
def get(access_token, topic, client_id, redirect_uri):
    spotifyUrl =  'https://api.spotify.com/v1/me/player'
    headers = {"Authorization": "Bearer " + str(access_token)}
    result = requests.get(spotifyUrl, headers=headers)

    if result.status_code == 204:
        # Playback not available or active
        return(204)
    elif result.status_code == 400:
        # Access Token Expired
        return(400)
    elif result.status_code == 200:
        try:
            result = requests.get(spotifyUrl, headers=headers)
            result = json.loads(result.content)

            print(result['item']['album']['name'])

            try:
                result_context_type = result['context']['type']
                result_context_uri = result['context']['uri']
            except:
                pass

            track_progress = result['progress_ms']
            track_total_duration = result['item']['duration_ms']

            # If track was paused, don't re-record
            track_percentage_played = round((track_progress / track_total_duration) * 100)

            result = {
                'songID': result['item']['id'],
                'song' : result['item']['name'],
                'artist' : result['item']['artists'][0]['name'],
                'playing' : result['is_playing'],
                'album' : result['item']['album']['name'],
                'albumID' : result['item']['album']['id'],
                'deviceID': result['device']['id'],
                'device': result['device']['name'],
                'deviceType': result['device']['type'],
                'contextType' : result_context_type,
                'contextUri' : result_context_uri
            }
            return(result)
        except:
            message = 'Fatal error at player.py. New status code?'
            notify.send_notfication(message, topic, client_id, redirect_uri)
            return(None)