import boto3
import os

def handler(event, context):
    table = os.environ['DynamoDBTable']
    print(f'Accessing {table}')