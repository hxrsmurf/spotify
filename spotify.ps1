function NotUsed{
	$uri = "https://accounts.spotify.com/api/token"
	$username = $null
	$password = $null
	$pair = "$($username):$($password)"
	$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
	$basicAuthValue = "Basic $encodedCreds"
}

function Authorization {
$authorizeURL = "https://accounts.spotify.com/authorize?"
	$redirectURL = "https://hxrsmurf.info"
	$scope = "user-modify-playback-state user-read-currently-playing user-read-playback-state"
	$clientId = $null
	$authorizeURL = $authorizeURL + "client_id=$clientid" + "&redirect_uri=$redirectURL" + "&scope=$scope" + "&response_type=token"
	$authorizeURL
}

function Player {

	$token = $args[0]
	$volume = $args[1]
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
	$headers.Add("Authorization", "Bearer $token")
	$playerURI = "https://api.spotify.com/v1/me/player"
	$uri = $playerURI + "/devices"
	$devices = Invoke-RestMethod -URI $uri -Headers $headers -Method GET
	$deviceActive = $devices.devices.is_active
	$deviceName = $devices.devices.name

	if ($deviceActive -eq $true) {
		echo "Checking playback on $deviceName"
		$uri = $playerURI
		$playback = Invoke-RestMethod -URI $uri -Headers $headers -Method GET		
		$track = $playback.item.name	
		$artist = $playback.item.artists.name
		
		if ($playback.item.artists.length -ne 1){
			$artist = $artist[0]
		}
		
		$nowPlaying =  "'$track' by '$artist'"
		
		if ($playback.is_playing -eq $false){
			echo "Start playing $nowPlaying on $deviceName"
			$uri = $playerURI + "/play"
			Invoke-RestMethod -URI $uri -Headers $headers -Method PUT			
		}  else {	
			echo "Pausing $nowPlaying on $deviceName"
			$uri = $playerURI + "/pause"
			Invoke-RestMethod -URI $uri -Headers $headers -Method PUT	
		}
		
		if ($playback.repeat_state -ne "context"){	
			echo "Turning on repeat."
			$uri = $playerURI + "/repeat"
			$uri = $uri + "?state=context"
			Invoke-RestMethod -URI $uri -Headers $headers -Method PUT	
		}
		
		if ($devices.devices[0].volume_percent -ne $volume){		
			$uri = $playerURI + "/volume"
			$uri = $uri + "?volume_percent=$volume"		
			Invoke-RestMethod -URI $uri -Headers $headers -Method PUT
		}		
	} else {
		echo "No devices found."
		return
	}
}