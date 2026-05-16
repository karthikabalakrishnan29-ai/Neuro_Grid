from fastapi import APIRouter

router = APIRouter()

@router.post("/simulate-blackout")
async def trigger_blackout():
    return {"message": "Simulating Grid Outage... Activating Island Mode."}