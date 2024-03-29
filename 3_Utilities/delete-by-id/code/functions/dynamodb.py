import boto3
import os

def db_delete(id):
    table = os.environ['Table']
    client = boto3.client('dynamodb')

    response = client.delete_item(
        TableName = table,
        Key = {
            'id' : {
                'S' : id
            }
        }
    )