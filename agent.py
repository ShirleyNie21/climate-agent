import json

print("🚀 RUNNING AGENT TEST")

data = {"readings": []}

data["readings"].append({
    "temperature": 999,
    "time": "TEST"
})

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("💾 WRITE COMPLETE")
