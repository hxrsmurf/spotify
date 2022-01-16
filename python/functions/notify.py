import boto3
import functions.ssm as ssm
import functions.authorization as authorization

# Notifies me via SNS if something goes bad.
def send_notfication(message, topic, client_id, redirect_uri):
    print(message)

    sns_client = boto3.client('sns')
    
    authURL = authorization.get_authorization(client_id, redirect_uri)

    message = str(message) + ' You may need to click the link below: \n'

    body = str(message) + authURL
    
    snsPublish = sns_client.publish(
                    TargetArn=topic,
                    Message=body,
                    Subject="AWS Spotify Tracker"
                )