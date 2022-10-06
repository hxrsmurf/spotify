import boto3
import os

def db_query():
    client = boto3.client('dynamodb')
    table = os.environ['DynamoDBTable']
    global_secondary_index = 'year_month-id-index'

    response = client.query(
        TableName = table,
        IndexName = global_secondary_index,
        KeyConditionExpression = 'year_month = :value',
        ExpressionAttributeValues = {
            ':value' : {
                'S' : '2022-10'
            }
        }
    )

    return response['Items']