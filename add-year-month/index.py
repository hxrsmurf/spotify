import boto3
import os

from datetime import datetime
from functions.dynamodb import db_put

def handler(event, context):
    table = os.environ['DynamoDBTable']
    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.scan(
        TableName=table
    )

    results = response['Items']

    for result in results:
        if not 'year_month' in result:
            id = result['id']['S']
            datetime_object = datetime.strptime(id, '%Y-%m-%d, %H:%M:%S:%f')
            year_month = datetime_object.strftime('%Y-%m')
            result_db_put = db_put(id, year_month)
            print(id, result_db_put)