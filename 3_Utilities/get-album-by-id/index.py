# This is a simple helper script to get album's image from Spotify, based on album id. 
# I have a custom internal table that I use, because my original collection did not collect album id
# Hacky workaround, for sure. But hey, it works.
# Get token by going to Spotify API Web and copying the network tab's fetch/curl/header
# Get AWS Token and paste
# Run it.

import boto3
import requests
import json
import ast

token = ""
headers = {"Authorization" : "Bearer " + token}
base_url = "https://api.spotify.com/v1/albums/"
table_top ='spotify-tracker-sam-DynamoDBTop-1VWZP135CNFSV'

def lookup(album_id):
    response = requests.get(base_url + album_id, headers=headers)
    result = json.loads(response.content)
    return result['images'][0]['url']

def query():
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.scan(
        TableName=table_top,
    )
    return response['Items']

def update(album_id, image):
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.update_item(
        TableName='spotify-tracker-sam-artist-id',
        Key={
            'artist': {
                'S': album_id
            }
        },
        AttributeUpdates={
            'album_image': { 'Value': {'S' : image } }
        }
    )
    status_code = response['ResponseMetadata']['HTTPStatusCode']

    if not status_code == 200:
        print('Error updating', artist)

results = query()

for album in results:
    al = album['top_albums']['S']
    json_album = ast.literal_eval(al)
    for j in json_album:
        album_id = j['albumID']
        album = j['album']
        album_image = lookup(album_id)
        update(album_id, album_image)
        print(album, album_image)