import requests
import json

# Endpoint URL
url = "https://clzut41m4.paperspacegradient.com/model-serving/des4z1prl34tt5o:predict"

# Request
payload = json.dumps({
  "customer": "u6746rt67h78",
  "transaction": {
    "transaction_amt": "410.0",
    "ip_add": "98.116.195.133",
    "billing_city": "New York City",
    "billing_postal": "11205",
    "currency": "usd",
    "cvv": "V",
    "click_speed": "0.3487",
    "transaction_env": "T",
    "tempo": "101.993",
    "valence": "0.443876228"
  }
})

headers = {
  'Content-Type': 'application/json',
  'cache-control': "no-cache"
}

response = requests.request("POST", url, headers=headers, data=payload)

# Response
print(response.text)
