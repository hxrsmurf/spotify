import functions.ssm as ssm

def parameters(output_keys):
    # I don't think a dictionary Case/Switch statement makes a lot of sense here. So, I'm not doing that.

    for output in output_keys:
        if output['OutputKey'] == 'RefreshToken':
            refresh_token = output['OutputValue']
        elif output['OutputKey'] == 'ClientSecret':
            client_secret = output['OutputValue']
        elif output['OutputKey'] == 'ClientID':
            client_id = output['OutputValue']
        elif output['OutputKey'] == 'RedirectUri':
            redirect_uri = output['OutputValue']
        elif output['OutputKey'] == 'CurrentTrack':
            current_track = output['OutputValue']
        elif output['OutputKey'] == 'Table':
            table = output['OutputValue']
        elif output['OutputKey'] == 'Topic':
            topic = output['OutputValue']
    
    # This returns the CFT's Output, which can contain the SSM Parameter ARN or the actual Resource ARN.
    return refresh_token, client_secret, client_id, redirect_uri, current_track, table, topic

def get(output_keys):
    refresh_token_parameter, client_secret_parameter, client_id_parameter, redirect_uri, current_track_parameter, table, topic = parameters(output_keys)
    
    refresh_token = ssm.get(refresh_token_parameter)
    refresh_token_parameter = refresh_token_parameter
    client_secret = ssm.get(client_secret_parameter)
    client_id = ssm.get(client_id_parameter)
    redirect_uri = redirect_uri
    current_track_parameter = current_track_parameter
    current_track = ssm.get(current_track_parameter)
    table = table
    topic = topic

    return refresh_token_parameter, refresh_token, client_secret, client_id, redirect_uri, current_track_parameter, current_track, table, topic