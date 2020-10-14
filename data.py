import requests
import json

url = "https://api.spotify.com/v1/browse/new-releases"

def getSpotifyData():
    data = requests.get(url, headers={"Authorization": "Bearer " + "BQA4PORFiWLhn1-F89As1yseIcyUNHpRr0swG5Ri-8W64iFROI0cwMlZDBGQruEnv6FmHlvsTwndEyvE-NI"})
    parsed_data = json.loads(data.text)
    return parsed_data

spotify_data = getSpotifyData()
arrData = spotify_data['albums']['items']
song_ids = []
for song in arrData[:5]:
    song_id = song['id']
    song_ids.append(song_id)
    print(song_id)

for song in song_ids:
    song_url = "https://api.spotify.com/v1/albums/" + song
    data = requests.get(song_url, headers={"Authorization": "Bearer " + "BQA4PORFiWLhn1-F89As1yseIcyUNHpRr0swG5Ri-8W64iFROI0cwMlZDBGQruEnv6FmHlvsTwndEyvE-NI"})
    parsed_data = json.loads(data.text)
    print(parsed_data)
