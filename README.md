# 🌡️ Temperature Agent (Automated AI System)

## Overview
This project is an automated Python agent that collects real-time temperature data and stores it over time using GitHub Actions.

The agent is designed to run independently without manual execution and stops automatically after 24 hours.

---

## 🔧 Features
- Real-time weather data (Open-Meteo API)
- Automatic scheduling via GitHub Actions
- Persistent memory using JSON
- 24-hour self-stopping rule
- Simple data analysis (average temperature)

---

## 🧠 Key Concept
The agent uses a stored `start_time` to enforce a time limit:

> If more than 24 hours pass, the agent stops automatically.

This demonstrates time-aware autonomous behavior.

---

## ⚙️ Tech Stack
- Python
- GitHub Actions
- Open-Meteo API
- JSON storage

---

## 📊 Output Example
- Temperature logs over time
- Average temperature calculation
- Timestamped readings

---

## 🚀 How it works
1. GitHub Actions runs the script every 30 minutes
2. Script fetches live temperature data
3. Data is stored in `data.json`
4. After 24 hours, the agent stops automatically

---

## 📌 Purpose
This project demonstrates:
- AI agent design
- Automation workflows
- Time-constrained systems
- Real-world API integration
- Persistent memory systems
