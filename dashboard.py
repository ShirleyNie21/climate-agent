import time
import json
import streamlit as st
import time

st.title("🌤️ Weather Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
with open("data.json", "r") as f:
    data = json.load(f)

readings = data["readings"]

st.write("Total readings:", len(readings))

# -------------------------
# REFRESH CONTROL
# -------------------------
if st.button("🔄 Refresh Data"):
    st.rerun()

auto_refresh = st.checkbox("Auto-refresh every 5 seconds")

# -------------------------
# LATEST READING
# -------------------------
st.subheader("📌 Latest Reading")

if len(readings) > 0:
    st.write(readings[-1])
else:
    st.write("No data yet — run agent.py first")

# -------------------------
# HISTORY CHART
# -------------------------
st.subheader("📊 Temperature History")

temps = [r["temperature"] for r in readings]

if len(temps) > 0:
    chart_data = {
        "Time": [r["time"][-8:] for r in readings],
        "Temperature": temps
    }
    
    st.line_chart(chart_data, x="Time", y="Temperature")
else:
    st.write("No data for chart yet")

# -------------------------
# STATS
# -------------------------
st.subheader("📈 Quick Stats")

if len(temps) > 0:
    st.write("Average:", sum(temps) / len(temps))
    st.write("Max:", max(temps))
    st.write("Min:", min(temps))
else:
    st.write("Not enough data yet — run agent.py first")

# -------------------------
# AUTO REFRESH (SAFE)
# -------------------------
if auto_refresh:
    time.sleep(5)
    st.rerun()

# auto refresh every 5 seconds
time.sleep(5)
st.rerun()
