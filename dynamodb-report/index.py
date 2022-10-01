import boto3
import os

def handler(event, context):
    table = os.environ['DynamoDBTable']
    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.scan(
        TableName=table
    )
    results = response['Items']
    if 'LastEvaluatedKey' in response:
        last_key = response['LastEvaluatedKey']
        print(last_key)

    print ('album', 'artist', 'song_id', 'device_id', 'device_type', 'device', 'id', 'album_id')
    for result in results:
        album = result['album']['S']
        artist = result['artist']['S']
        song_id = result['songID']['S']
        device_id = result['deviceID']['S']
        device_type = result['deviceType']['S']
        device = result['device']['S']
        id = result['id']['S']
        album_id = result['albumID']['S']
        print (album, artist, song_id, device_id, device_type, device, id, album_id)