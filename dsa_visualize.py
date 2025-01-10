import requests
import base64
import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

CLIENT_ID  = "46edae514d864282b93a788cabe6fce1"
CLIENT_SECRET  = "e3e94d8f2fbf4787b68e39e3f8364e3c"


TOKEN_URL = "https://accounts.spotify.com/api/token"

moods = {
    "anadolu rock": 0.7,
    "turkish pop": 1.0,
    "turkish rock": 0.7,
    "classical": 0.1,
    "early romatic era": 0.1,
    "irish classical": 0.1,
    "german romaticisim": 0.1,
    "late romantic era": 0.1,
    "polish classical": 0.1,
    "turkce trap metal":0.5,
    "turkish psych": 0.8,
    "turkish singer-songwriter": 0.7,
    "arabesk": 0.0,
    "classic turkish pop": 0.5,
    "turkish jazz": 0.3,
    "turkish hip hop": 0.8,
    "turkish trap": 0.9,
    "turkce drill": 0.9,
    "turkish folk": 0.6,
    "turkish alt pop": 0.4,
    "turkish instrumental": 0.5,
    "turkish slow sarkılar": 0.3
}

def get_access_token(client_id, client_secret):
   
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

   
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None


access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Access token alınamadı.")

with open('spotify_data.json', 'r') as file:
    data = json.load(file)

def getInfo(uri, acces):
    headers = {
        "Authorization": f"Bearer {acces}"
    }

    response = requests.get(uri, headers=headers)
    if response.status_code == 200:
        return response.json()["genres"]
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None
    

music_data = {
    "name": [],
    "datetime": [],
    "genres": [],
    "popularity": []
}
for item in data:
    music_data["name"].append(item["track"]["name"])
    music_data["datetime"].append(item["played_at"].split("T")[0])
    music_data["genres"].append(getInfo(item["track"]["artists"][0]["href"], access_token))
    music_data["popularity"].append(item["track"]["popularity"])


with open('weather.json', 'r') as file:
    data = json.load(file)

weather_data = {
    "date": [],
    "temp": []
}
for item in data["days"]:
    weather_data["date"].append(item["datetime"])
    weather_data["temp"].append(item["feelslike"])

weather_df = pd.DataFrame(weather_data)
music_df = pd.DataFrame(music_data)

print(weather_df.info())
print(music_df.info())
music_df['date'] = pd.to_datetime(music_df['datetime']).dt.date
weather_df['date'] = pd.to_datetime(weather_df['date']).dt.date


avg_popularity = music_df.groupby('date')['popularity'].mean().reset_index()
avg_popularity.rename(columns={'popularity': 'avg_popularity'}, inplace=True)


all_genres = music_df.groupby('date')['genres'].sum().reset_index()
all_genres['genre_count'] = all_genres['genres'].apply(lambda x: Counter([genre for sublist in x for genre in sublist]))

merged_data = pd.merge(weather_df, avg_popularity, on='date', how='left')


plt.figure(figsize=(10, 6))
plt.scatter(merged_data['temp'], merged_data['avg_popularity'], color='blue')
plt.title('Günlük Ortalama Sıcaklık ve Ortalama Popülerlik')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Ortalama Popülerlik')
plt.grid()
plt.show()

merged_df = pd.merge(music_df, weather_df, on='date', how='left')


genre_temp_data = []
for temp, genres in zip(merged_df['temp'], merged_df['genres']):
    for genre in genres:
        genre_temp_data.append({'temp': temp, 'genre': genre})

genre_temp_df = pd.DataFrame(genre_temp_data)

heatmap_data = genre_temp_df.pivot_table(index='genre', columns='temp', aggfunc='size', fill_value=0)


plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="coolwarm")
plt.title('Sıcaklık ve Müzik Türleri İlişkisi')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Müzik Türleri')
plt.show()


music_df['date'] = pd.to_datetime(music_df['datetime']).dt.date
weather_df['date'] = pd.to_datetime(weather_df['date']).dt.date


def calculate_avg_mood(genres):
    mood_values = [moods[genre] for genre in genres if genre in moods]
    return sum(mood_values) / len(mood_values) if mood_values else 0

music_df['avg_mood'] = music_df['genres'].apply(calculate_avg_mood)
daily_mood = music_df.groupby('date')['avg_mood'].mean().reset_index()

merged_df = pd.merge(weather_df, daily_mood, on='date', how='left')


plt.figure(figsize=(10, 6))
plt.scatter(merged_df['temp'], merged_df['avg_mood'], color='purple')
plt.title('Sıcaklık ve Günlük Ortalama Mood İlişkisi')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Günlük Ortalama Mood')
plt.grid()
plt.show()