# ⚡ Neuro_Grid — Intelligent Digital Twin Framework for Hybrid Microgrids

> 🎓 Final Year Major Project | B.E – Electrical & Electronics Engineering  
> 🏫 University VOC College of Engineering, Thoothukudi | 2022–2026  
> 👩‍💻 Developed by **Karthika B**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?style=for-the-badge&logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?style=for-the-badge&logo=fastapi)
![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-black?style=for-the-badge&logo=apachekafka)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?style=for-the-badge&logo=kubernetes)
![MQTT](https://img.shields.io/badge/MQTT-IoT_Protocol-purple?style=for-the-badge)

---

## 🌟 Project Overview

**Neuro_Grid** is a production-grade, AI-driven **Digital Twin** platform for hybrid renewable microgrids (Solar + Wind + Battery). It mirrors physical grid behavior in real time, predicts failures before they occur, forecasts energy demand, and simulates disaster scenarios — all from a unified Streamlit dashboard.

This project is architected like a **real-world SCADA/EMS platform**, featuring a full 9-layer modular system including IoT ingestion, Kafka streaming, FastAPI backend, ML intelligence, Digital Twin simulation, security, monitoring, and market trading.

### 🔋 Microgrid Specifications
| Energy Source | Capacity / Status |
|--------------|-------------------|
| ☀️ Solar | 45.8 kW monitored |
| 💨 Wind | Real-time generation tracked |
| 🔋 Battery | State of Charge (SOC) monitored |
| 🏠 Load | Live demand tracking + 24hr forecasting |

---

## 🏗️ System Architecture — 9-Layer Design

```
┌─────────────────────────────────────────────────────────┐
│           📊 Visualization Layer (Streamlit)            │
│  8 Dashboards: Executive | IoT | Forecasting | Twin    │
│        Fault | Scenario | Control | AI Hub             │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│               🌐 API Layer (FastAPI)                    │
│  Routes: /forecast | /anomaly | /twin | /scenario      │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│             🧠 Intelligence Layer                       │
│  Anomaly Detection | EMS | Explainability | Topology   │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                  ⚙️ Core Layer                          │
│  Digital Twin | Forecasting (LSTM+XGBoost) | Assets    │
│  Simulation | Optimization (MILP + RL Agent)           │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
┌───────────┐  ┌──────────────┐  ┌───────────────┐
│ 📡 IoT   │  │ 🔄 Streaming │  │ 🎯 Scenario   │
│  Layer   │  │    Layer     │  │   Engine      │
│  MQTT +  │  │ Kafka Prod/  │  │ Fault Inject  │
│  Edge    │  │  Consumer    │  │ Disaster Sim  │
└───────────┘  └──────────────┘  └───────────────┘
        │
        ▼
┌────────────────────────────────────────────────────────┐
│  🔐 Security  |  📈 Monitoring  |  🏪 Market Layer    │
│  AES + RBAC  |  Prometheus +   |  Trading Agent +    │
│  Secure MQTT |  Grafana        |  Demand Response    │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### 📊 8 Real-Time Streamlit Dashboards
| Dashboard | Description |
|-----------|-------------|
| 🏢 Executive Dashboard | KPIs, daily savings, carbon offset overview |
| 📡 IoT Live Monitor | Real-time Solar, Wind, Battery, Load data |
| 🤖 AI Forecasting | 24-hr demand prediction (LSTM + XGBoost) |
| 🧬 Digital Twin Lab | Virtual microgrid replica & simulation |
| 🔍 Fault Analytics | ML-based fault classification + anomaly scoring |
| 🧪 Scenario Lab | Grid Blackout, Solar Eclipse, Voltage Sag simulation |
| 🎛️ Control Center | Actuator control & setpoint management |
| 🧠 AI Decision Hub | Explainable AI decisions & energy optimization |

### 🤖 Intelligence Layer
- **Anomaly Detection** — ML fault classification with real-time scoring & alert prioritization
- **Root Cause Analysis** — Automated diagnosis of grid faults
- **Energy Management System (EMS)** — Cost calculator, tariff engine, energy dispatch
- **Explainability (XAI)** — Transparent, explainable AI decisions
- **Topology Optimizer** — Smart grid graph optimization

### ⚙️ Core Layer
- **Digital Twin** — Shadow device, sync engine, twin state, API bridge
- **Forecasting** — LSTM + XGBoost ensemble for load, solar & wind prediction
- **Optimization** — MILP optimizer + Reinforcement Learning agent
- **Simulation** — Energy balance, power flow, grid stability engine
- **Assets** — Solar panel, wind turbine, battery, load, diesel generator models

### 📡 IoT + Streaming
- **MQTT** — Real-time sensor data with QoS handling & topic management
- **Edge Processing** — Edge aggregation and filtering
- **Apache Kafka** — High-throughput producer/consumer streaming pipeline

### 🔐 Security + Monitoring
- **AES Encryption + RBAC** — Role-based access control, secure MQTT (TLS)
- **Prometheus + Grafana** — Full system health monitoring

### 🏪 Market Layer
- **Price Simulator** — Dynamic energy pricing engine
- **Trading Agent** — Automated grid energy trading
- **Demand Response** — Load flexibility & demand management

---

## 💰 Economic Impact Metrics

| Metric | Value |
|--------|-------|
| 💵 Daily Savings | ₹1,240 |
| 🌿 Carbon Offset | 4.2 Tons |
| ⚡ Grid Export Revenue | Tracked & Visualized |

---

## 📁 Project Structure

```
📦 Neuro_Grid/
 ┣ 📂 api_layer/             # FastAPI REST endpoints & schemas
 ┣ 📂 core_layer/            # Digital Twin, Forecasting, Optimization
 ┣ 📂 intelligence_layer/    # Anomaly Detection, EMS, XAI, Topology
 ┣ 📂 iot_layer/             # MQTT, Edge Processing, Sensor Simulator
 ┣ 📂 streaming_layer/       # Apache Kafka pipeline
 ┣ 📂 visualization_layer/   # 8 Streamlit dashboards + components
 ┣ 📂 scenario_engine/       # Disaster & fault simulation
 ┣ 📂 security_layer/        # Auth, AES encryption, RBAC
 ┣ 📂 market_layer/          # Trading, pricing, demand response
 ┣ 📂 monitoring/            # Prometheus + Grafana config
 ┣ 📂 deployment/            # Docker + Kubernetes configs
 ┣ 📂 models/                # Trained ML model files (.pkl)
 ┣ 📂 data/                  # Raw, processed & sample datasets
 ┣ 📂 docs/                  # Architecture & flow diagrams
 ┣ 📂 tests/                 # Unit & integration tests
 ┣ 📂 scripts/               # Data processing & training scripts
 ┣ 📜 main.py                # Application entry point
 ┗ 📜 requirements.txt       # Python dependencies
```

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Neuro_Grid.git
cd Neuro_Grid

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the dashboard
streamlit run visualization_layer/app_main.py
```

### 🐳 Docker
```bash
docker-compose up --build
```

---

## 📦 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.10+ |
| **Dashboard** | Streamlit 1.32, Plotly 5.19 |
| **API** | FastAPI 0.110, Uvicorn |
| **ML / AI** | Scikit-learn, LSTM, XGBoost, RL Agent, MILP |
| **IoT** | MQTT (paho-mqtt), Edge Processing |
| **Streaming** | Apache Kafka (kafka-python) |
| **Security** | AES Encryption, RBAC, Secure MQTT |
| **Monitoring** | Prometheus, Grafana |
| **Deployment** | Docker, Kubernetes |
| **Data** | Pandas 2.2, NumPy 1.26 |

---

## 🏆 Achievements

- ✅ Built a **9-layer, production-grade EMS** comparable to real-world SCADA platforms
- ✅ Implemented **Apache Kafka** streaming pipeline for high-throughput real-time data
- ✅ Designed **Digital Twin** with Grid Blackout, Solar Eclipse & Voltage Sag simulations
- ✅ Built **AI forecasting** (LSTM + XGBoost ensemble) predicting 24-hour energy demand
- ✅ Integrated **MILP Optimizer + RL Agent** for intelligent energy dispatch
- ✅ Deployed with **Docker + Kubernetes** with Prometheus + Grafana monitoring
- ✅ Implemented **AES encryption + RBAC** security with Secure MQTT

---

## 👩‍💻 Developer

**Karthika B**  
🔗 [LinkedIn](https://www.linkedin.com/in/karthika-b-86379929a/) | 📧 karthikabalakrishnan29@gmail.com  
📍 Thoothukudi, Tamil Nadu, India

---

> ⭐ If you found this project impressive, give it a star!

