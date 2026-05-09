import json
import streamlit as st

st.title("🌤️ Weather Dashboard")

# load data
with open("data.json", "r") as f:
    data = json.load(f)

readings = data["readings"]

# latest reading
st.subheader("📌 Latest Reading")
if len(readings) > 0:
    st.write(readings[-1])
else:
    st.write("No data yet — run agent.py first")

# history
st.subheader("📊 Temperature History")
temps = [r["temperature"] for r in readings]
st.line_chart(temps)

# stats
st.subheader("📈 Quick Stats")

if len(temps) > 0:
    st.write("Average:", sum(temps) / len(temps))
    st.write("Max:", max(temps))
    st.write("Min:", min(temps))
else:
    st.write("Not enough data yet — run agent.py first")
