import json
import requests
from datetime import datetime, timedelta

# load data
with open("data.json", "r") as f:
    data = json.load(f)

# set start time if not set yet
if data["start_time"] is None:
    data["start_time"] = datetime.utcnow().isoformat()

start_time = datetime.fromisoformat(data["start_time"])
current_time = datetime.utcnow()

# check 24-hour rule
elapsed = current_time - start_time

if elapsed > timedelta(hours=24):
    print("⛔ 24 hours passed. Agent stopping.")
    exit()

# 🌡️ REAL TEMPERATURE DATA (THIS IS THE PART YOU WERE MISSING)
lat = 40.71
lon = -74.00

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
weather = response.json()

temperature = weather["current_weather"]["temperature"]

# store reading
data["readings"].append({
    "time": current_time.isoformat(),
    "temperature": temperature
})

print("✅ Temperature recorded:", temperature)

# save back
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
