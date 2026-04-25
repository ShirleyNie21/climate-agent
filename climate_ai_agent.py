import requests
import json
from datetime import datetime

# =========================
# 1. LOAD MEMORY (history)
# =========================
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []


# =========================
# 2. FETCH API DATA (observe)
# =========================
url = "https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&current_weather=true"
response = requests.get(url)
weather = response.json()


# =========================
# 3. EXTRACT CURRENT VALUE
# =========================
current_temp = weather["current_weather"]["temperature"]


# =========================
# 4. CREATE NEW RECORD
# =========================
new_entry = {
    "temperature": current_temp,
    "time": datetime.now().isoformat(),
    "location": "Summit"
}


# =========================
# 5. GET PAST CONTEXT (compare inputs)
# =========================
previous_temp = data[-1]["temperature"] if len(data) > 0 else None

max_temp = max([d["temperature"] for d in data]) if len(data) > 0 else current_temp


# =========================
# 6. DECISION LOGIC (agent brain)
# =========================
alert = False

print("Current temperature:", current_temp)
print("Previous temperature:", previous_temp)
print("Max temperature so far:", max_temp)

if previous_temp is not None:
    if current_temp > previous_temp:
        print("📈 Temperature is rising")
    elif current_temp < previous_temp:
        print("📉 Temperature is falling")
    else:
        print("➡️ Temperature is stable")

if current_temp > max_temp:
    print("🔥 NEW RECORD HIGH!")
    alert = True


# attach decision to memory
new_entry["alert"] = alert


# =========================
# 7. SAVE MEMORY (store history)
# =========================
data.append(new_entry)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
