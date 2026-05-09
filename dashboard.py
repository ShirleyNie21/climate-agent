import json
import streamlit as st

st.title("🌤️ Weather Dashboard")

with open("data.json", "r") as f:
    data = json.load(f)

readings = data["readings"]

st.subheader("📌 Latest Reading")
latest = readings[-1]
st.write(latest)

st.subheader("📊 Temperature History")
temps = [r["temperature"] for r in readings]
st.line_chart(temps)

st.subheader("📈 Quick Stats")

st.write("Average:", sum(temps) / len(temps))
st.write("Max:", max(temps))
st.write("Min:", min(temps))
