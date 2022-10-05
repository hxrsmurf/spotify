import boto3
import os

def db_delete(id):
    table = os.environ['DynamoDBTable']

    print(id)