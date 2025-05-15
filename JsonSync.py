import json
import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer dein_token"
}

payload = {
    "key": "value"
}

response = requests.post("https://192.168.4.1/control", data=json.dumps(payload), headers=headers)
