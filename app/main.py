from datetime import datetime

from fastapi import FastAPI
from starlette import status

from app.model.event.power_state_update import PowerStateUpdateEvent
from app.model.request.track_request import TrackRequest
from app.queue import power_state_update

app = FastAPI()


@app.post("/api/power/state", status_code=status.HTTP_201_CREATED)
async def track_api(req: TrackRequest):
    power_state_update.send(
        PowerStateUpdateEvent(device_id=req.device_id, state=req.power_state, fired_at=datetime.now()))

    return {}
