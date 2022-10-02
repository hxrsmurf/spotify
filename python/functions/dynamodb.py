import boto3
from datetime import datetime
import functions.ssm as ssm

def put(now_playing, table, current_track_parameter):
    # Some ids will be eastern and some will be UTC
    dt = datetime.utcnow()
    timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')
    epoch_time = dt.timestamp()

    # Allows for cleaning up the database
    print(f'Timestamp: {timestamp}')
    print(f'epoch_time: {epoch_time}')

    recent_track = ssm.get(current_track_parameter)

    play_state = now_playing['playing']

    if not play_state:
        print(f'Play state is {play_state}')
    else:
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
                },
                'album': {
                    'Value': {
                        'S': now_playing['album']
                    }
                },
                'albumID': {
                    'Value': {
                        'S': now_playing['albumID']
                    }
                },
                'deviceID': {
                    'Value': {
                        'S': now_playing['deviceID']
                    }
                },
                'device': {
                    'Value': {
                        'S': now_playing['device']
                    }
                },
                'deviceType': {
                    'Value': {
                        'S': now_playing['deviceType']
                    }
                },
                'epochTime': {
                    'Value': {
                        'N': str(epoch_time)
                    }
                },
                'contextType': {
                    'Value': {
                        'S': now_playing['contextType']
                    }
                },
                'contextUri': {
                    'Value': {
                        'S': now_playing['contextUri']
                    }
                },
                'trackDurationMS': {
                    'Value': {
                        'N': now_playing['trackDuration']
                    }
                }
            }
        )
        ssm.put(current_track_parameter, now_playing['songID'])