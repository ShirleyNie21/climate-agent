import json
from datetime import datetime

print("🚀 Agent started")

FILE = "data.json"

# load existing file
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

print("📂 Loaded:", data)

# ensure key exists
if "readings" not in data:
    data["readings"] = []

# your temperature (you already have this from API)
temp = 13.1

print("🌡️ Temperature:", temp)

# THIS is the critical missing step
data["readings"].append({
    "temp": temp,
    "time": datetime.now().isoformat()
})

print("🧠 Updated data:", data)

# write back to file
with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("💾 Saved to file")
