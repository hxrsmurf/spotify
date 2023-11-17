import boto3
import os

# table = os.environ['Table']
table = 'spotify-tracker-sam-DynamoDB-153V5770W5PY5'
client = boto3.client('dynamodb', region_name='us-east-1')
index = 'year_month-id-index'

def query(year_month):
    response = client.query(
        TableName=table,
        IndexName=index,
        Limit=10,
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

    return response['Items']