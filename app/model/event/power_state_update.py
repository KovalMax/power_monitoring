import datetime

from pydantic import BaseModel

from app.model.enum.power_state import PowerStateEnum


class PowerStateUpdateEvent(BaseModel):
    device_id: str
    state: PowerStateEnum
    fired_at: datetime
