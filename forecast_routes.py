from fastapi import APIRouter

router = APIRouter()

@router.get("/load-prediction")
async def get_load_forecast():
    # Prediction values from LSTM/XGBoost
    return {"next_1h_load": 12.5, "unit": "kW", "confidence": 0.94}