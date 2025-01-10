import requests
import json
url = "https://accounts.spotify.com/authorize?client_id=46edae514d864282b93a788cabe6fce1&response_type=code&redirect_uri=http://localhost:3000/callback&scope=user-read-recently-played"



CLIENT_ID = "46edae514d864282b93a788cabe6fce1"
CLIENT_SECRET = "e3e94d8f2fbf4787b68e39e3f8364e3c"
AUTH_CODE = "AQDGncCcbhyE7u15dv21wmmDW6Am-eT3HjCzRCNpmPtbhV444-oBDP0anepRtY6qZTaz0p8wnyOFISU0L7Bar87KsOsiAzljKquO2j2v-3kA7FdB-2EQTGblbJ50LFZ3QRKqxaFWvWoS89d18qzsp4eM13Yh85llYM0cX5nDsexo-9DeQnHBQTEC2aT9XQJ76v5ZYwh4lFvzWB7jdw"

TOKEN_URL = "https://accounts.spotify.com/api/token"

def get_access_token(auth_code, client_id, client_secret, redirect_uri):
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None


access_token = get_access_token(AUTH_CODE, CLIENT_ID, CLIENT_SECRET, "http://localhost:3000/callback")


if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Access token alınamadı.")
def get_recently_played(access_token):
    params = {
    "limit": 50
}
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None



music_list = []

recently_played = get_recently_played(access_token)
if(recently_played):
    for item in recently_played["items"]:
        music_list.append(item)

with open("spotify_data.json", "w") as file:
    json.dump(music_list, file)
        


    

