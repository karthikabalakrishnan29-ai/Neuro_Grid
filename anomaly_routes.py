from fastapi import APIRouter

router = APIRouter()

@router.get("/alerts")
async def get_alerts():
    return [
        {"type": "Voltage Spike", "severity": "Medium", "timestamp": "2026-04-02T11:00Z"},
        {"type": "Normal", "severity": "Low", "timestamp": "2026-04-02T11:05Z"}
    ]