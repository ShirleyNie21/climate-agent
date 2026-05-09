import json
from datetime import datetime

FILE = "data.json"

# load existing data
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

# make sure structure exists
if "readings" not in data:
    data["readings"] = []

# new reading
new_reading = {
    "temp": 13.1,
    "time": datetime.now().isoformat()
}

# append it
data["readings"].append(new_reading)

# save back
with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("✅ Saved reading")
