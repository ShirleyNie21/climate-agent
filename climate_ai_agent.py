import requests
import json
from datetime import datetime

# Load memory
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []

# Fetch API data
url = "https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&current_weather=true"
response = requests.get(url)
weather = response.json()

current_temp = weather["current_weather"]["temperature"]

# Create new entry
new_entry = {
    "temperature": current_temp,
    "time": datetime.now().isoformat(),
    "location": "Summit"
}

# Get previous and max
previous_temp = data[-1]["temperature"] if len(data) > 0 else None
max_temp = max([d["temperature"] for d in data]) if len(data) > 0 else current_temp

# Decision logic
print("Current:", current_temp)
print("Previous:", previous_temp)
print("Max so far:", max_temp)

if previous_temp is not None:
    if current_temp > previous_temp:
        print("📈 Temperature is rising")
    elif current_temp < previous_temp:
        print("📉 Temperature is falling")
    else:
        print("➡️ Temperature is stable")

if current_temp > max_temp:
    print("🔥 NEW RECORD HIGH!")

# Save updated memory
data.append(new_entry)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
