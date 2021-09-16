import requests
import json

# Endpoint URL
url = "https://clzut41m4.paperspacegradient.com/model-serving/des4z1prl34tt5o:predict"

# Request
payload = json.dumps({
  "acousticness": 0.344719513,
  "danceability": 0.758067547,
  "energy": 0.323318405,
  "instrumentalness": 0.0166768347,
  "liveness": 0.0856723112,
  "speechiness": 0.0306624283,
  "tempo": 101.993,
  "valence": 0.443876228
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Response
print(response.text)
