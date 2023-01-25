import os
import boto3

client = boto3.client('dynamodb')

def put_item(playlist_id):
    response = client.put_item(
        TableName = os.environ['TableName'],
        Item = {
            'id' : {
                'S' : playlist_id
            }
        }
    )

    print(response)