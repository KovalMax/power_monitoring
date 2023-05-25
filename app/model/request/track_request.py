from pydantic import BaseModel

from app.model.enum.power_state import PowerStateEnum


class TrackRequest(BaseModel):
    device_id: str
    power_state: PowerStateEnum
    battery_level: float
    network_level: int
    fired_at: float | None
