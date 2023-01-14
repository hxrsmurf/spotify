import boto3
import functions.ssm as ssm
import functions.authorization as authorization
import os

# Notifies me via SNS if something goes bad.

def send_notfication(message, topic, client_id, redirect_uri):
    print(message)

    sns_client = boto3.client('sns')

    authURL = authorization.get_authorization(client_id, redirect_uri)

    body = str(message)

    if not message == '502':
        message = str(message) + ' You may need to click the link below: \n'
        body = str(message) + authURL

    snsPublish = sns_client.publish(
        TargetArn=topic,
        Message=body,
        Subject="AWS Spotify Tracker"
    )

def send_test_notification():
    message = 'Testing'
    topic = os.environ['Topic']

    client = boto3.client('sns')
    client.publish(
        TargetArn=topic,
        Message=message,
        Subject='AWS Spotify Tracker'
    )