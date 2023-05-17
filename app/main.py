from fastapi import FastAPI
from starlette import status

from app.model.request.track_request import TrackRequest
from app.queue import power_state_update

app = FastAPI()


@app.post("/api/power/state", status_code=status.HTTP_201_CREATED)
async def track_api(req: TrackRequest):
    power_state_update.send(req.json())

    return {}
