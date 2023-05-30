from dataclasses import dataclass

from app.model.enum.power_state import PowerStateEnum


@dataclass
class PowerStateUpdateEvent:
    device_id: str
    power_state: PowerStateEnum
    battery_level: float
    network_level: int
    fired_at: float

    def __post_init__(self):
        if len(self.device_id) <= 0 or self.device_id == '':
            raise ValueError('Can not be empty')

        if not isinstance(self.power_state, PowerStateEnum):
            self.power_state = PowerStateEnum(self.power_state)