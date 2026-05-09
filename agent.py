import json
from datetime import datetime

data = []

new_entry = {
    "temp": 13.1,
    "time": datetime.now().isoformat()
}

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []

data.append(new_entry)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
