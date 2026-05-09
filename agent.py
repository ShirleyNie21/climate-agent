cat > agent.py << 'EOF'
import json
import os
from datetime import datetime

print("🚀 CLEAN AGENT RUNNING")

FILE = os.path.join(os.path.dirname(__file__), "data.json")

# load safely
try:
    with open(FILE, "r") as f:
        data = json.load(f)
except:
    data = {"readings": []}

temp = 13.4

print("🌡️ Temp:", temp)

data["readings"].append({
    "temperature": temp,
    "time": datetime.now().isoformat()
})

with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print("💾 SAVED SUCCESSFULLY")

with open(FILE, "r") as f:
    print("📂 FINAL FILE:", json.load(f))
EOF
