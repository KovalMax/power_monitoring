from dataclasses import dataclass

from app.model.enum.power_state import PowerStateEnum


@dataclass
class EventModel:
    device_id: str
    power_state: PowerStateEnum
    battery_level: float
    network_level: int
    created_at: int
    updated_at: int

    def to_dict(self):
        return self.__dict__.copy()
