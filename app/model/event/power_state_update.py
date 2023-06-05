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
        if self.device_id is None or len(self.device_id) <= 0:
            raise ValueError('Can not be empty')

        if self.power_state is None:
            raise ValueError('Can not be empty')

        if self.battery_level is None:
            raise ValueError('Can not be empty')

        if self.network_level is None:
            raise ValueError('Can not be empty')

        if self.fired_at is None or self.fired_at <= 0:
            raise ValueError('Can not be empty')

        if not isinstance(self.power_state, PowerStateEnum):
            self.power_state = PowerStateEnum(self.power_state)
