# This is a simple helper script to get artist's image from Spotify, based on artist id. 
# I have a custom internal table that I use, because my original collection did not collect artist id
# Hacky workaround, for sure. But hey, it works.
# Get token by going to Spotify API Web and copying the network tab's fetch/curl/header
# Get AWS Token and paste
# Run it.

import boto3
import requests
import json

token = ""
headers = {"Authorization" : "Bearer " + token}
base_url = "https://api.spotify.com/v1/artists/"

def lookup(artist_id):
    response = requests.get(base_url + artist_id, headers=headers)
    result = json.loads(response.content)
    return result['images'][0]['url']

def query():
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.scan(
        TableName='spotify-tracker-sam-artist-id'
    )
    return response['Items']

def update(artist, image):
    client = boto3.client('dynamodb', region_name='us-east-1')
    response = client.update_item(
        TableName='spotify-tracker-sam-artist-id',
        Key={
            'artist': {
                'S': artist
            }
        },
        AttributeUpdates={
            'artist_image': { 'Value': {'S' : image } }
        }
    )
    status_code = response['ResponseMetadata']['HTTPStatusCode']

    if not status_code == 200:
        print('Error updating', artist)

artists = query()

for artist in artists:
    id = artist['id']['S']
    artist = artist['artist']['S']
    artist_image = lookup(id)
    update(artist, artist_image)
    print(artist, artist_image)