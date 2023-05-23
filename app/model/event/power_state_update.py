from dataclasses import dataclass
from app.model.enum.power_state import PowerStateEnum


@dataclass
class PowerStateUpdateEvent:
    device_id: str
    power_state: PowerStateEnum
    fired_at: float
