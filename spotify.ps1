function initialScope {
	$client_id = ""
	$client_secret = ""	

	$accounts_url = "https://accounts.spotify.com/"
	$authorizeURL = $accounts_url + "authorize?"

	$clientString = "client_id=" + $client_id
	$responseString = "&response_type=code&redirect_uri="
	$redirect_uri = "https://kvchmurphy.com/callback/"
	
	# https://developer.spotify.com/documentation/general/guides/scopes/
	$scope = (
	"user-read-recently-played",
	"user-top-read",
	"user-read-playback-position",
	"user-read-playback-state",
	"user-modify-playback-state",
	"user-read-currently-playing",
	"app-remote-control",
	"streaming",
	"playlist-modify-public",
	"playlist-modify-private",
	"playlist-read-private",
	"playlist-read-collaborative",
	"user-follow-modify",
	"user-follow-read",
	"user-library-modify",
	"user-library-read",
	"user-read-email",
	"user-read-private" )

	$scopeString = "&scope=$scope"

	$authorizeURL = $authorizeURL + $clientString + $responseString + $redirect_uri + $scopeString
	
	# https://marckean.com/2015/09/21/use-powershell-to-make-rest-api-calls-using-json-oauth/
	$ie = New-Object –comObject InternetExplorer.Application
	$ie.visible = $true
	$ie.navigate($authorizeURL)
	do{ Start-Sleep 1 } until ( $ie.LocationURL -match 'code=([^&]*)' )
	$code = $matches[1]
	$ie.Quit()
	return $code
}

function getRefreshToken {
	$client_id = ""
	$client_secret = ""
	$base64String = $client_id + ":" + $client_secret
	$base64 = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($base64String))
	
	$redirect_uri = "https://kvchmurphy.com/callback/"
	$refresh_url = "https://accounts.spotify.com/api/token"
	
	$headers = @{
		"Authorization" = "Basic $base64"
	}
	
	$code = initialScope
	
	$data = @{
		grant_type = "authorization_code"
		code = $code
		redirect_uri = "$redirect_uri"
	}

	$request = Invoke-WebRequest -URI $refresh_url -Method "POST" -Headers $headers -body $data
	$request = $request.content | ConvertFrom-JSON
	
	$output = @{
		access_token = $null
		refresh_token = $null
		expires_in = $null
	}

	$output.access_token = $request.access_token
	$output.refresh_token = $request.refresh_token
	$output.expires_in = $request.expires_in
	
	return $output
}

function refreshToken ($refresh_token) {
	$data = @{
			grant_type = "refresh_token"
			refresh_token = $refresh_token
	}
	
	$refresh_url = "https://accounts.spotify.com/api/token"
	$request = Invoke-WebRequest -URI $refresh_url -Method "POST" -Headers $headers -body $data
	$request = $request.content | ConvertFrom-JSON
	
	$access_token = $request.access_token
	
	return $access_token
}

function getUser ($access_token) {
	$user_url = "https://api.spotify.com/v1/me"

	$headers = @{
		"Authorization" = "Bearer $access_token"
	}

	$request = Invoke-WebRequest -URI $user_url -Headers $headers
	$request = $request.content | ConvertFrom-JSON
	return $request
}

function getTop ($access_token){
	$base_top_url = "https://api.spotify.com/v1/me/top/"
	
	$headers = @{
		"Authorization" = "Bearer $access_token"
	}

	# artists or tracks
	$type = "tracks"
	
	<#
		time_range
		long_term = several years
		medium_term = 6-months
		short_term = 4-weeks
	#>
	
	$time_range = "short_term"
	$limit = 50
	
	$top_url = $base_top_url + $type + "?time_range=$time_range&limit=$limit"
	
	$request = Invoke-WebRequest -URI $top_url -headers $headers
	$request = $request.content | ConvertFrom-JSON
	$items = $request.items
	
	foreach ($item in $items){
		if ($type = "tracks"){
			 Write-Host $item.name "-" $item.artists.name
		} else {
			Write-Host $item.name
		}
	}
}

function modifyPlayback ($access_token) {
	$headers = @{
		"Authorization" = "Bearer $access_token"
	}
	
	$player_url = "https://api.spotify.com/v1/me/player"
	$request = Invoke-WebRequest -URI $player_url -headers $headers
	$request = $request.content | ConvertFrom-JSON
	
	if ($request.is_playing -eq $true){
		$playback_url = "https://api.spotify.com/v1/me/player/pause"
	} else {
		$playback_url = "https://api.spotify.com/v1/me/player/play"
	}
	
	$request = Invoke-WebRequest -URI $playback_url -Method "PUT" -Headers $headers
}

function getPlayer ($access_token){
	$headers = @{
		"Authorization" = "Bearer $access_token"
	}
	
	$player_url = "https://api.spotify.com/v1/me/player"
	$request = Invoke-WebRequest -URI $player_url -Method "GET" -Headers $headers
	$request = $request.content | ConvertFrom-JSON
	return $request
	
}

function getPlaylists ($access_token){
	$headers = @{
		"Authorization" = "Bearer $access_token"
	}
	
	$playlists_url = "https://api.spotify.com/v1/me/playlists" + "?limit=50"
	$request = Invoke-WebRequest -URI $playlists_url -Method "GET" -Headers $headers
	$request = $request.content | ConvertFrom-JSON
	$items = $request.items
	
	foreach ($item in $items){
		if ($item.name -like "Daily Mix*"){
			Write-Host $item.name "|" $item.external_urls.spotify "|" $item.href
		}
	}
}

function login {
	if ($refresh_token){
		$access_token = refreshToken $refresh_token
	} else {
		if ($access_token -eq $null -or $refresh_token -eq $null){
			$getTokens = getRefreshToken
			$refresh_token = $getTokens.refresh_token
			$access_token = $getTokens.access_token
		}
	}
	
	# Need to fix this, so only refresh token if needed.
	
	$refreshToken = getRefreshToken $refresh_token
	$refresh_token = $refreshToken.refresh_token
	$access_token = $refreshToken.access_token
	
	return $access_token
}