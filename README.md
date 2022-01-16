# spotify (Python Lambda)

Note: This incurs AWS charges. I am not liable for any damages or costs.

The `spotify.py` is console based and manual. The `lambda.py` is the lambda version of this. The `spotify.yaml` is the AWS CloudFormation template which creates:

- DynamoDB (to store the Spotify track ID, track name, and artist name)
- EventBridge Rule (to Invoke the Lambda every 5-minutes)
- Lambda (basic Python code to get refresh token and get player) 
- Log Group (for Lambda to write to, 3 day retention)
- Systems Manager Parameters (Spotify Client ID, Spotify Client Secret, and Refresh Token)
- IAM Role and relevant Policies so this can function (Lambda, CloudWatch, SSM, and SNS)
- SNS Topic/Subscription for any issues (haven't had my refresh token expire yet, so who knows)

## Manual Steps Required:

1. Get Spotify Refresh Token (get the URL w/ client id, get the token, get your first auth token)
2. Upload Requests Lambda Layer

## Procedure for CFT Deployment:

1. Update the Systems Manager Parameters with the appropriate client ID, client secret, and refresh token
2. Launch the Stack in AWS CloudFormation
3. Confirm your e-mail (SNS Subscription)
4. Complete

# Guides I used:
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
- https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
- https://developer.spotify.com/documentation/web-api/reference/#/operations/get-information-about-the-users-current-playback

# spotify (PowerShell)

This is a basic PowerShell to control Spotify's Player and get top track/artist report.

The functions...don't work, so keep that in mind.

Load PowerShell:

```
. .\spotify.ps1
```

1. Authorization
2. Paste in web browser
3. Get token (grab from after access_token to &token_type)
	- https://hxrsmurf.info/#access_token=MYTOKEN&token_type=Bearer&expires_in=3600
	- MYTOKEN
4. player MYTOKEN 100
	- 100 is the volume
 
