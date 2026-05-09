cat > agent.py << 'EOF'
import requests
import json
from datetime import datetime

print("🚀 Agent started")

lat = 40.71
lon = -74.00

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print("🌐 API response received")

temperature = data["current_weather"]["temperature"]

print("🌡️ Temperature:", temperature)
EOF
