from datetime import datetime

from pydantic import BaseModel

from app.model.enum.power_state import PowerStateEnum


class TrackRequest(BaseModel):
    device_id: str
    power_state: PowerStateEnum
    fired_at: datetime = datetime.now()

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp()
        }
