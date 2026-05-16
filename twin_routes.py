from fastapi import APIRouter

router = APIRouter()

@router.get("/current-state")
async def get_twin_state():
    # Inga Digital Twin state logic-a call pannanum
    return {
        "solar_kw": 15.4,
        "wind_kw": 8.2,
        "battery_soc": 72.5,
        "grid_status": "Connected"
    }