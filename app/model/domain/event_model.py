from dataclasses import dataclass, asdict


@dataclass
class EventModel:
    device_id: str
    power_state: int
    battery_level: float
    network_level: int
    created_at: int
    updated_at: int

    def to_dict(self):
        return self.__dict__.copy()
