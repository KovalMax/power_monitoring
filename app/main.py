from datetime import datetime

from fastapi import FastAPI
from starlette import status

from app.model.request.track_request import TrackRequest
from app.queue import power_state_update

app = FastAPI()


@app.post("/api/power/state", status_code=status.HTTP_201_CREATED)
async def track_api(req: TrackRequest):
    if not req.fired_at:
        req.fired_at = datetime.utcnow().timestamp()

    power_state_update.send(req.dict())

    return {}
