import boto3
from datetime import datetime
import os

def put(id, epoch_time):
    table = os.environ['DynamoDBTable']

    print(f'Updating {id} with {epoch_time}')

    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName=table,
        Key={
            'id': {
                'S': id
            }
        },
        AttributeUpdates={
                'epochTime': {
                        'Value': {
                            'N': str(epoch_time)
                        }
                }
        }
    )