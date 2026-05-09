import json
import os

print("🚀 TEST START")

FILE = os.path.join(os.path.dirname(__file__), "data.json")

print("📍 Writing to:", FILE)

data = {"readings": []}

data["readings"].append({
    "temperature": 999,
    "time": "TEST"
})

print("💾 About to write...")

with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("✅ WRITE DONE")

# verify immediately
with open(FILE, "r") as f:
    check = json.load(f)

print("📂 AFTER WRITE:", check)
