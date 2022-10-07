import boto3
import os

def s3_upload(file):
    bucket = os.environ['Bucket']
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(file, bucket, 'destination.csv')