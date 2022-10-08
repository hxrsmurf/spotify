import boto3
import os
from datetime import datetime

from functions.dynamodb import put
from functions.sns import send_notfication

def handler(event, context):
    table = os.environ['Table']
    print(f'Accessing {table}')

    client = boto3.client('dynamodb')
    response = client.scan(
        TableName=table,
        Limit=1
    )

    results = response['Items']

    for result in results:
        if not 'epochTime' in result:
            id = result['id']['S']
            datetime_object = datetime.strptime(id, '%Y-%m-%d, %H:%M:%S:%f')
            epoch_time = (datetime_object).timestamp()

            put(id, epoch_time)

    send_notfication()