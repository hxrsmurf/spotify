import boto3
import os
from datetime import datetime

from functions.dynamodb import db_delete

def handler(event, context):
    table = os.environ['DynamoDBTable']
    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.query(
        TableName=table,
        Limit=1
    )