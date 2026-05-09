import json
from datetime import datetime

FILE = "data.json"

# 1. Load existing data
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

# 2. Create new reading
new_reading = {
    "temp": 13.1,
    "time": datetime.now().isoformat()
}

# 3. Append it properly
data["readings"].append(new_reading)

# 4. Save back
with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("✅ Saved:", new_reading)
