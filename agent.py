cat > agent.py << 'EOF'
import json
import os
from datetime import datetime
import requests

print("🚀 Agent started")

FILE = os.path.join(os.path.dirname(__file__), "data.json")

# load file safely
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

lat = 40.71
lon = -74.00

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data_api = response.json()

print("🌐 API response received")

temperature = data_api["current_weather"]["temperature"]

print("🌡️ Temperature:", temperature)

data["readings"].append({
    "temperature": temperature,
    "time": datetime.now().isoformat()
})

with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("💾 Saved to file")

with open(FILE, "r") as f:
    print("📂 Final data:", json.load(f))
EOF
