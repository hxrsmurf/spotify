import boto3
import os

from .utils import current_year_month, previous_month

def db_query():
    client = boto3.client('dynamodb')
    table = os.environ['Table']
    global_secondary_index = 'year_month-id-index'

    response = client.query(
        TableName = table,
        IndexName = global_secondary_index,
        #Limit = 1,
        KeyConditionExpression = 'year_month = :value',
        ExpressionAttributeValues = {
            ':value' : {
                'S' : previous_month()
            }
        }
    )

    items_counted = response['Count']
    items_scanned = response['ScannedCount']

    try:
        last_key = response['LastEvaluatedKey']
        print(f'Last Key: {last_key}')
    except:
        pass

    print(f'Count: {items_counted}')
    print(f'Scanned: {items_scanned}')

    return response['Items']