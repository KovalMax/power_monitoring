import datetime

from app.model.enum.power_state import PowerStateEnum


class PowerStateUpdateEvent:
    def __init__(self, device_id: str, state: PowerStateEnum, fired_at: datetime):
        self.device_id = device_id
        self.state = state
        self.fired_at = fired_at
