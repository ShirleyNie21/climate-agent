import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&current_weather=true"

response = requests.get(url)

data = response.json()

print(data)
