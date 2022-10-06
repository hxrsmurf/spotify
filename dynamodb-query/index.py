import boto3
import os

def handler(event, context):
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

    for results in response['Items']:
        print(results['id']['S'])