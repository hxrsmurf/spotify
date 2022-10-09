import boto3
import os

def send_notfication(message):
    topic = os.environ['Topic']
    sns_client = boto3.client('sns')

    snsPublish = sns_client.publish(
        TargetArn=topic,
        Message=message,
        Subject="AWS Spotify Tracker - Export Started"
    )