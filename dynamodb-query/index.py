import boto3
import os

def index(event, context):
    client = boto3.client('dynamodb')
    table = os.environ['DynamoDBTable']
    global_secondary_index = 'year_month-index'

    response = client.query(
        TableName = table,
        IndexName = global_secondary_index
    )

    for results in response:
        print(results)