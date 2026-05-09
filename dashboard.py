import json
import streamlit as st

st.title("🌤️ Weather Dashboard")

# -------------------------
# LOAD DATA (SAFE)
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
# MANUAL REFRESH
# -------------------------
if st.button("🔄 Refresh Data"):
    st.rerun()

auto_refresh = st.checkbox("Auto-refresh every 5 seconds")

# -------------------------
# LATEST READING
# -------------------------
st.subheader("📌 Latest Reading")

if readings:
    st.write(readings[-1])
else:
    st.write("No data yet — run agent.py first")

# -------------------------
# CHART
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

    st.write("Average:", sum(temps) / len(temps))
    st.write("Max:", max(temps))
    st.write("Min:", min(temps))
else:
    st.write("Not enough data yet — run agent.py first")

# -------------------------
# AUTO REFRESH (OPTIONAL ONLY)
# -------------------------
if auto_refresh:
    import time
    time.sleep(5)
    st.rerun()
