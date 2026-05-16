from fastapi import APIRouter

router = APIRouter()

@router.get("/market/price")
async def get_market_price():
    # Price simulator-la irunthu price edukka
    return {"current_price": 7.45, "currency": "INR", "unit": "kWh"}

@router.post("/market/trade")
async def execute_trade(volume_kwh: float, trade_type: str):
    # Buy/Sell order execute panna
    return {"status": "Trade Executed", "volume": volume_kwh, "type": trade_type}