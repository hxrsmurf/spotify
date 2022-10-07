import boto3
import os

from .utils import current_year_month

def db_query():
    client = boto3.client('dynamodb')
    table = os.environ['DynamoDBTable']
    global_secondary_index = 'year_month-id-index'

    response = client.query(
        TableName = table,
        IndexName = global_secondary_index,
        Limit = 10,
        KeyConditionExpression = 'year_month = :value',
        ExpressionAttributeValues = {
            ':value' : {
                'S' : current_year_month()
            }
        }
    )

    items_counted = response['Count']
    items_scanned = response['ScannedCount']

    print(f'Count: {items_counted}')
    print(f'Scanned: {items_scanned}')

    return response['Items']