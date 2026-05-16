# ⚡ Intelligent Digital Twin Framework for Hybrid Microgrids
**Design and Implementation of an AI-Driven Digital Twin for Renewable Energy Systems.**

---

## 📖 Project Overview
This project implements a high-fidelity **Digital Twin** for a Hybrid Microgrid (Solar, Wind, Battery). It leverages a 4-layer architecture—IoT, Simulation, Intelligence (ML), and Visualization—to monitor, predict, and control energy assets in real-time.

### ✨ Key Features
* **Real-time Mirroring:** Synchronization between physical sensor data and virtual models.
* **AI Forecasting:** Load demand and Solar generation prediction using **Random Forest**.
* **Fault Analytics:** Automated anomaly detection and health monitoring.
* **Economic Dispatch:** Dynamic energy pricing and market-driven control.
* **Scenario Lab:** "What-if" stress testing for grid resilience (Blackouts, Cyber-attacks).

---

## 🏗️ System Architecture
The framework is organized into a modular structure for scalability:

- **`api_layer/`**: FastAPI endpoints for data exchange.
- **`core_layer/`**: Mathematical models and Digital Twin state logic.
- **`intelligence_layer/`**: Machine Learning models for forecasting and fault detection.
- **`iot_layer/`**: MQTT-based sensor data simulation and streaming.
- **`visualization_layer/`**: Interactive Streamlit Dashboard with SVG schematics.
- **`scenario_engine/`**: Stress testing and resilience analysis scripts.
- **`security_layer/`**: AES encryption and Role-Based Access Control (RBAC).

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.9+** and **Anaconda** installed.
```bash
pip install streamlit fastapi uvicorn pandas scikit-learn paho-mqtt plotly joblib cryptography