import json
import streamlit as st

st.title("🌤️ Weather Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("No data.json found. Run agent.py first.")
    st.stop()

readings = data.get("readings", [])

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

if readings:
    latest = readings[-1]

    st.metric(
        label="Current Temperature",
        value=f"{latest['temperature']} °C"
    )

from datetime import datetime

formatted_time = datetime.fromisoformat(
    latest["time"]
).strftime("%b %d, %Y • %I:%M %p")

st.caption(f"Last updated: {formatted_time}")
else:
    st.write("No data yet — run agent.py first")

# -------------------------
# TEMPERATURE CHART
# -------------------------
st.subheader("📊 Temperature History")

if readings:
    temps = [r["temperature"] for r in readings]

    chart_data = {
        "Temperature": temps
    }

    st.line_chart(chart_data)
else:
    st.write("No data for chart yet")

# -------------------------
# STATS
# -------------------------
st.subheader("📈 Quick Stats")

if readings:
    temps = [r["temperature"] for r in readings]

    col1, col2, col3 = st.columns(3)

    col1.metric("Average", f"{sum(temps)/len(temps):.1f} °C")
    col2.metric("Max", f"{max(temps):.1f} °C")
    col3.metric("Min", f"{min(temps):.1f} °C")
else:
    st.write("Not enough data yet — run agent.py first")

# -------------------------
# AUTO REFRESH
# -------------------------
if auto_refresh:
    import time
    time.sleep(5)
    st.rerun()
