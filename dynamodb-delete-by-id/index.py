import boto3
import os
from datetime import datetime

from functions.dynamodb import db_delete

def handler(event, context):
    table = os.environ['DynamoDBTable']
    value = '2022-10-02, 00:05:58:782681'

    with open('ids.txt', 'r') as ids_to_delete:
        for id in ids_to_delete:
            print(f'Deleting {id}...')
            db_delete(id)

    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.query(
        TableName=table,
        KeyConditionExpression='id = :value',
        ExpressionAttributeValues={
            ':value' : {
                'S' : value
            }
        }
    )

    print(response)