import boto3
import os

from datetime import datetime
import functions.ssm as ssm
from functions.utils import calculate_duration_since_last_entry, current_year_month_day, current_timestamp_epoch

def put(now_playing, table, current_track_parameter):
    # Some ids will be eastern and some will be UTC
    dt = datetime.utcnow()
    timestamp = dt.strftime('%Y-%m-%d, %H:%M:%S:%f')
    year_month = dt.strftime('%Y-%m')
    epoch_time = dt.timestamp()
    PreviousEntryEpochTime = os.environ['PreviousEntryEpochTime']
    now_playing_track = now_playing['songID']
    now_playing_track_duration = now_playing['trackDuration']
    possible_duplicate = False

    # Allows for cleaning up the database
    print(f'Timestamp: {timestamp}')
    print(f'epoch_time: {epoch_time}')

    recent_track = ssm.get(current_track_parameter)
    recent_entry = ssm.get(PreviousEntryEpochTime)

    duration_since_last_entry_ms = calculate_duration_since_last_entry(previous=recent_entry, current=epoch_time)
    print(f'Duration since last: {duration_since_last_entry_ms / 1000} seconds')

    if now_playing_track == recent_track:
        print(f'This track may already be recorded: {now_playing["songID"]}')
        difference_between_last_and_track_duration = (duration_since_last_entry_ms / now_playing_track_duration) * 100
        possible_duplicate = True

    play_state = now_playing['playing']

    if not play_state:
        print(f'Play state is {play_state}')
    else:
        ssm.put(parameter=current_track_parameter, value=now_playing['songID'])
        ssm.put(parameter=PreviousEntryEpochTime,value=str(epoch_time))

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
                        'N': str(now_playing['trackDuration'])
                    }
                },
                'possibleDuplicate': {
                    'Value': {
                        'BOOL': possible_duplicate
                    }
                },
                'year_month': {
                    'Value': {
                        'S': year_month
                    }
                }
            }
        )

def db_put_refresh_token(refresh_token):
    client = boto3.client('dynamodb')
    table = os.environ['TableRefreshToken']
    timestamp, epoch_time = current_timestamp_epoch()

    response = client.update_item(
        TableName=table,
        Key={
            'id': {
                'N': str(epoch_time)
            }
        },
        AttributeUpdates={
            'refresh_token': {
                'Value': {
                 'S': refresh_token
                }
            },
            'year_month_day': {
                'Value' : {
                    'S' : current_year_month_day()
                }
            },
            'timestamp': {
                'Value' : {
                    'S' : timestamp
                }
            }
        }
    )

    print(f'Refresh Token Update: {response}')