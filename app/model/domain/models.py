from dataclasses import dataclass

from app.model.enum.power_state import PowerStateEnum


@dataclass
class EventModel:
    device_id: str
    power_state: PowerStateEnum
    battery_level: float
    network_level: int
    created_at: int

    def __post_init__(self):
        if self.device_id is None or len(self.device_id) <= 0:
            raise ValueError('device_id: can not be empty')

        if self.power_state is None:
            raise ValueError('power_state: can not be empty')

        if self.battery_level is None:
            raise ValueError('battery_level: can not be empty')

        if self.network_level is None:
            raise ValueError('network_level: can not be empty')

        if self.created_at is None or self.created_at <= 0:
            raise ValueError('created_at: can not be empty')

        if not isinstance(self.power_state, PowerStateEnum):
            self.power_state = PowerStateEnum(self.power_state)

    def to_dict(self):
        return {
            'deviceId': self.device_id,
            'powerState': self.power_state,
            'batteryLevel': self.battery_level,
            'networkLevel': self.network_level,
            'createdAt': self.created_at,
        }


@dataclass
class DeviceModel:
    id: str
    active: int
    user_id: str
    device_id: str
    device_name: str

    def to_dict(self):
        return self.__dict__.copy()
