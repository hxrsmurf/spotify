import boto3
import os

from .utils import current_day_time

def db_export():
    table = os.environ['Table']
    bucket = os.environ['Bucket']
    client = boto3.client('dynamodb')
    outut_file = f'{current_day_time}.csv'

    response = client.export_table_to_point_in_time(
        TableName = table,
        S3Bucket = bucket,
        S3Prefix = f'output/{outut_file}'
    )

    print(response)