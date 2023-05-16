from fastapi import FastAPI
from pydantic import BaseModel



class TrackRequest(BaseModel):
    deviceId: str
    powerState: int


app = FastAPI()


@app.post("/track")
async def track_api(req: TrackRequest):
    print(req)

    return {}
