# 🔌 Microgrid Digital Twin API Documentation

## Base URL
`http://localhost:8000`

## Endpoints

### 1. Digital Twin State
* **URL:** `/api/twin/current-state`
* **Method:** `GET`
* **Response:** Returns real-time Solar, Wind, and Battery metrics.

### 2. Load Forecasting
* **URL:** `/api/forecast/load-prediction`
* **Method:** `GET`
* **Response:** Predicted load for the next 1 hour (LSTM Model).

### 3. Anomaly Detection
* **URL:** `/api/anomaly/alerts`
* **Method:** `GET`
* **Response:** List of detected faults (Voltage spikes, Frequency drops).

### 4. Control Interface
* **URL:** `/api/control/switch-relay`
* **Method:** `POST`
* **Payload:** `{"device_id": "string", "status": "boolean"}`