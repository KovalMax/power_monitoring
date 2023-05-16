from pydantic import BaseModel


class TrackRequest(BaseModel):
    deviceId: str
    powerState: int
