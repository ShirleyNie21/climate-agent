import requests
import json
from datetime import datetime

# 1. Load existing memory (history)
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []

# 2. Call Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&current_weather=true"
response = requests.get(url)
weather = response.json()

# 3. Extract temperature
temp = weather["current_weather"]["temperature"]

# 4. Create new record
new_entry = {
    "temperature": temp,
    "time": datetime.now().isoformat(),
    "location": "Summit"
}

# 5. Append to memory
data.append(new_entry)

# 6. Save back to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# 7. Print latest value
print("Current temperature:", temp)
print("Total records stored:", len(data))
