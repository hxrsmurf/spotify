import boto3
import os

from datetime import datetime
from functions.dynamodb import db_put

def handler(event, context):
    table = os.environ['Table']
    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.scan(
        TableName=table,
        ExclusiveStartKey= {
            'id' : {
                'S' :'00-00-00, 00:00:00:000000'
                }
        }
    )

    results = response['Items']

    for result in results:
        if not 'year_month' in result:
            id = result['id']['S']
            datetime_object = datetime.strptime(id, '%Y-%m-%d, %H:%M:%S:%f')
            year_month = datetime_object.strftime('%Y-%m')
            result_db_put = db_put(id, year_month)
            print(id, result_db_put)

    try:
        message = 'LastKey', response['LastEvaluatedKey']
        print(message)
        return(message)
    except:
        message = 'No last key!'
        print(message)
        return(message)