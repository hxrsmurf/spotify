import boto3
import os
import ast
from .utils import get_current_year_month

# table = os.environ['Table']
table = 'spotify-tracker-sam-DynamoDB-153V5770W5PY5'
table_top ='spotify-tracker-sam-DynamoDBTop-1VWZP135CNFSV'
table_artist ='spotify-tracker-sam-artist-id'

client = boto3.client('dynamodb', region_name='us-east-1')
index = 'year_month-id-index'

def query(year_month):
    list_items = []

    paginator = client.get_paginator('query')
    response = paginator.paginate(
        TableName=table,
        IndexName=index,
        KeyConditionExpression='year_month = :year_month',
        FilterExpression='possibleDuplicate = :duplicate',
        ExpressionAttributeValues={
            ':year_month': {
                'S': year_month,
            },
            ':duplicate': {
                'BOOL': False
            }
        }
    )

    for page in response:
        for item in page['Items']:
            list_items.append(item)
    
    return list_items

def get(year_month):
    response = client.get_item(
        TableName=table_top,
        Key={
            'id': {
                'S': year_month,
            }
        }
    )
    if 'Item' in response and not year_month == get_current_year_month():
        data = {
            "year_month": response['Item']['id']['S'],
            "top_devices": ast.literal_eval(response['Item']['top_devices']['S']),
            "top_songs": ast.literal_eval(response['Item']['top_songs']['S']),
            "top_artists": ast.literal_eval(response['Item']['top_artists']['S']),
            "top_albums": ast.literal_eval(response['Item']['top_albums']['S']),
            "top_playlists": ast.literal_eval(response['Item']['top_playlists']['S']),
        }
        return data
    else:
        return False

def put(year_month, data):
    if not get(year_month):
        print(f'Writing to Top Table {year_month}')
        response = client.put_item(
            TableName=table_top,
            Item={
                "id": {
                    "S": year_month,
                },
                "top_devices": {
                    "S": str(data['top_devices'])
                },
                "top_songs": {
                    "S": str(data['top_songs'])
                },
                "top_artists": {
                    "S": str(data['top_artists'])
                },
                "top_albums": {
                    "S": str(data['top_albums'])
                },
                "top_playlists": {
                    "S": str(data['top_playlists'])
                },
            }
        )

def get_artist_id(artist):
    response = client.get_item(
        TableName=table_artist,
        Key={
            'artist': {
                'S': artist,
            }
        }
    )

    if 'Item' in response:
        return response['Item']['artist_image']['S']
    else:
        return None