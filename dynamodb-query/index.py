import boto3
import os

def handler(event, context):
    client = boto3.client('dynamodb')
    table = os.environ['DynamoDBTable']
    global_secondary_index = 'year_month-index'

    response = client.query(
        TableName = table,
        IndexName = global_secondary_index,
        KeyConditions={
            'year_month' : {
                'AttributeValueList' : [
                    {
                        'S' : '2022-10'
                    }
                ],
                'ComparisonOperator' : 'EQ'
            }
        }
    )

    for results in response:
        print(results)