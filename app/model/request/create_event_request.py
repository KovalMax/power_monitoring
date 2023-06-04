from datetime import datetime

from pydantic import BaseModel, validator

from app.model.enum.power_state import PowerStateEnum


class CreateStateEventRequest(BaseModel):
    device_id: str
    power_state: PowerStateEnum
    battery_level: float
    network_level: int
    fired_at: float | None

    @validator('fired_at')
    def set_fired_at(cls, value):
        return datetime.utcnow().timestamp() if value is None else value
