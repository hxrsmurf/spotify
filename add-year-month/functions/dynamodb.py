import boto3
import os

def db_put(id, year_month):
    table = os.environ['DynamoDBTable']
    client = boto3.client('dynamodb')

    print(f'Updating {id} with {year_month}')

    return client.update_item(
        TableName=table,
        Key={
            'id': {
                'S': id
            }
        },
        AttributeUpdates={
                'year_month': {
                        'Value': {
                            'S': str(year_month)
                        }
                }
        }
    )