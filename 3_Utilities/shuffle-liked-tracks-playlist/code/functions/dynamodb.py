import os
import boto3

client = boto3.client('dynamodb')

def put_item(playlist_information):
    id = playlist_information['id']
    name = playlist_information['name']
    url = playlist_information['external_urls']['spotify']
    snapshot_id = playlist_information['snapshot_id']

    response = client.put_item(
        TableName = os.environ['TableName'],
        Item = {
            'id' : {
                'S' : id
            },
            'name' : {
                'S' : name
            },
            'url' : {
                'S': url
            },
            'snapshot_id' : {
                'S' : snapshot_id
            },
        }
    )