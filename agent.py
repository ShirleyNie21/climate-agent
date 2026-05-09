import json
from datetime import datetime

FILE = "data.json"

print("🚀 Agent started")

# load file
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

# ensure structure
if "readings" not in data:
    data["readings"] = []

# fake or real temp (keep yours if you already have API value)
temp = 13.1

print("🌡️ Temp:", temp)

# append new reading
data["readings"].append({
    "temp": temp,
    "time": datetime.now().isoformat()
})

print("🧠 Updated data:", data)

# force write
with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("💾 WROTE TO FILE")
