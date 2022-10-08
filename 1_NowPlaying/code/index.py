import os
import boto3
import json
from requests.auth import HTTPBasicAuth
import requests
import functions.ssm as ssm
import functions.authorization as authorization
import functions.player as player
import functions.dynamodb as dynamodb
import functions.notify as notify
import functions.eventbridge as eventbridge
import functions.ssm as ssm
import base64

def handler(event, context):
    # Not sure why I have to do this, but whatever.
    event = json.dumps(event)
    event = json.loads(event)

    # Grab EventBridge and set it to GET
    try:
        api_method = event['routeKey']
    except:
        api_method = 'GET /'

    if api_method == 'POST /':
        event_body = str((base64.b64decode(event['body'])), "utf-8")
        eventbridge.update(event_body)
        return {
            'statusCode' : 200,
            'body' : event_body
        }

    elif api_method == 'GET /':
        spotify_refresh_token_parameter = os.environ['SpotifyRefreshToken']
        spotify_refresh_token_parameter_value = ssm.get(spotify_refresh_token_parameter)

        client_id = ssm.get(os.environ['SpotifyClientID'])
        client_secret = ssm.get(os.environ['SpotifyClientSecret'])

        redirect_uri = os.environ['RedirectUri']

        current_track_parameter = os.environ['CurrentTrack']

        table = os.environ['Table']
        topic = os.environ['Topic']

        notify.send_notfication(message, topic, client_id, redirect_uri)
        return

        access_token = authorization.get_refresh_token(spotify_refresh_token_parameter_value, client_id, client_secret, spotify_refresh_token_parameter)['access_token']

        now_playing = (player.get(access_token, topic, client_id, redirect_uri))

        if now_playing == 204:
            print('Nothing playing')
        elif now_playing:
           record_now_playing = dynamodb.put(now_playing, table, current_track_parameter)
           return {
               'statusCode' : 200,
               'body' : json.dumps(now_playing)
           }
        else:
            message = 'Fatal error at index.py. Maybe a new status code?'
            notify.send_notfication(message, topic, client_id, redirect_uri)
    else:
        message = 'API Method failure'
        return {
            'statusCode': 200,
            'body': message
        }