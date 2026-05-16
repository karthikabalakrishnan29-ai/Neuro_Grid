from pydantic import BaseModel
from typing import List, Optional

class TwinState(BaseModel):
    solar_kw: float
    wind_kw: float
    load_kw: float
    battery_soc: float
    grid_status: str

class ForecastResponse(BaseModel):
    prediction: float
    unit: str = "kW"
    confidence: float

class AnomalyAlert(BaseModel):
    id: str
    type: str
    severity: str
    timestamp: str

class ControlAction(BaseModel):
    device_id: str
    action: str # "ON", "OFF", "CHARGE", "DISCHARGE"