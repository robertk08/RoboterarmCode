import requests

url = "https://example.com/api"
data = {
    "name": "Alice",
    "age": 30
}

response = requests.post(url, json=data)  # `json=` konvertiert automatisch zu JSON

print("Status:", response.status_code)
print("Antwort:", response.text)
