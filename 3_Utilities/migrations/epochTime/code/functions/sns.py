from email import message
import boto3
import os

def send_notfication():
    topic = os.environ['Topic']
    sns_client = boto3.client('sns')

    message = 'Updating DynamoDB with EPOCH is complete.'

    snsPublish = sns_client.publish(
                    TargetArn=topic,
                    Message=message,
                    Subject="AWS Spotify Tracker - EPOCH Time"
                )