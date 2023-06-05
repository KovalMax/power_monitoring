import logging

import dramatiq

from app.dependencies.dependecies import get_event_service, get_device_service, get_rabbitmq
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.service.device_service import DeviceService
from app.service.event_service import EventService

rabbitmq_broker = get_rabbitmq()
dramatiq.set_broker(rabbitmq_broker)

event_service: EventService = get_event_service()
device_service: DeviceService = get_device_service()


@dramatiq.actor
def power_state_update(update_event: dict[str, str | float]):
    try:
        event_model = PowerStateUpdateEvent(**update_event)
    except ValueError as e:
        logging.exception(str(e))
        return

    if not device_service.device_exists(event_model.device_id):
        return

    event_service.create_new_event(event_model)
