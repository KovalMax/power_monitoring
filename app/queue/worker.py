from os import environ

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from app.firebase.firebase_client import device_exists, create_new_event
from app.model.domain.event_model import EventModel
from app.model.event.power_state_update import PowerStateUpdateEvent

rabbitmq_broker = RabbitmqBroker(url=environ.get("BROKER_HOST"))
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def power_state_update(update_event: dict[str, str | float]):
    e = PowerStateUpdateEvent(**update_event)
    if not device_exists(e.device_id):
        return

    create_new_event(EventModel(device_id=e.device_id, power_state=e.power_state, network_level=e.network_level,
                                battery_level=e.battery_level, created_at=e.fired_at, updated_at=e.fired_at))
