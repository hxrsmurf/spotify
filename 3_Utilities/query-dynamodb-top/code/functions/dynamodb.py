import boto3
import os

# table = os.environ['Table']
table = 'spotify-tracker-sam-DynamoDB-153V5770W5PY5'
client = boto3.client('dynamodb', region_name='us-east-1')
index = 'year_month-id-index'

def query(year_month):
    list_items = []

    paginator = client.get_paginator('query')
    response = paginator.paginate(
        TableName=table,
        IndexName=index,
        KeyConditionExpression='year_month = :year_month',
        FilterExpression='possibleDuplicate = :duplicate',
        ExpressionAttributeValues={
            ':year_month': {
                'S': year_month,
            },
            ':duplicate': {
                'BOOL': False
            }
        }
    )


    for page in response:
        for item in page['Items']:
            list_items.append(item)
    
    return list_items