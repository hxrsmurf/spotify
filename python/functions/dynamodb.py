import boto3
from datetime import datetime
import functions.ssm as ssm

def put(now_playing, table, current_track_parameter):    
    # Set timestamp as 2022-01-10 18:59:00:00
    dt = datetime.now()
    timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')

    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName=table,
        Key={
            'id': {
                'S': timestamp
            }
        },
        AttributeUpdates={
            'songID': {
                'Value': {
                    'S': now_playing['songID']
                }
            },
            'song': {
                'Value': {
                    'S': now_playing['song']
                }
            },
            'artist': {
                'Value': {
                    'S': now_playing['artist']
                }
            }
        }
    )
    ssm.put(current_track_parameter, now_playing['songID'])