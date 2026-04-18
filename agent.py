import json
from datetime import datetime

# load data
with open("data.json", "r") as f:
    data = json.load(f)

# set start time if not set yet
if data["start_time"] is None:
    data["start_time"] = datetime.utcnow().isoformat()

current_time = datetime.utcnow().isoformat()

print("Start time:", data["start_time"])
print("Current time:", current_time)

# save back
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
