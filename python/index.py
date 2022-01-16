import os
import boto3
import json
from requests.auth import HTTPBasicAuth
import requests
import functions.cloudformation_output as cloudformation_output
import functions.ssm as ssm
import functions.authorization as authorization
import functions.player as player
import functions.dynamodb as dynamodb
import functions.notify as notify

def handler(event, context):
    client = boto3.client('cloudformation')
    response = client.describe_stacks(
        StackName='spotify-tracker-sam'
    )
    
    output_keys = response['Stacks'][0]['Outputs']
    
    refresh_token_parameter, refresh_token, client_secret, client_id, redirect_uri, current_track_parameter, current_track, table, topic = cloudformation_output.get(output_keys)

    access_token = authorization.get_refresh_token(refresh_token, client_id, client_secret, refresh_token_parameter)['access_token']

    now_playing = (player.get(access_token))

    if now_playing == 204:
        print('Nothing playing')
    elif now_playing:
       record_now_playing = dynamodb.put(now_playing, table, current_track_parameter)
       return('Complete')
    else:
        message = 'Fatal error at index.py. Maybe a new status code?'
        notify.send_notfication(message, topic, client_id, redirect_uri)