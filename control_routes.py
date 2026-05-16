from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/switch-relay")
async def control_relay(device_id: str, status: bool):
    # IoT layer-ku relay switch command anupa
    return {"status": "Success", "device": device_id, "state": "ON" if status else "OFF"}