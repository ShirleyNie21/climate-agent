import requests
import json
from datetime import datetime

print("🚀 Agent started")

# load existing data
with open("data.json", "r") as f:
    data_store = json.load(f)

lat = 40.71
lon = -74.00

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print("🌐 API response received")

temperature = data["current_weather"]["temperature"]

print("🌡️ Temperature:", temperature)

# append new reading
data_store["readings"].append({
    "time": datetime.utcnow().isoformat(),
    "temperature": temperature,
    "location": "Summit"
})

# save back to file
with open("data.json", "w") as f:
    json.dump(data_store, f, indent=2)
