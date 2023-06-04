from os import environ

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from fastapi import Depends

from app.dependencies.dependecies import get_event_service, get_device_service
from app.model.domain.event_model import EventModel
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.service.device_service import DeviceService
from app.service.event_service import EventService

rabbitmq_broker = RabbitmqBroker(url=environ.get("BROKER_HOST"))
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def power_state_update(update_event: dict[str, str | float], event_service: EventService = Depends(get_event_service),
                       device_service: DeviceService = Depends(get_device_service)):
    e = PowerStateUpdateEvent(**update_event)
    if not device_service.device_exists(e.device_id):
        return

    model = EventModel(device_id=e.device_id, power_state=e.power_state, network_level=e.network_level,
                       battery_level=e.battery_level, created_at=e.fired_at, updated_at=e.fired_at)

    event_service.create_new_event(model)
