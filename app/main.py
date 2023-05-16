from fastapi import FastAPI
from app.model.request.track_request import TrackRequest

app = FastAPI()


@app.post("/track")
async def track_api(req: TrackRequest):
    print(req)

    return {}
