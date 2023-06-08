import logging

import dramatiq

from app.dependencies.dependecies import get_event_service, get_device_service, get_rabbitmq, get_notification_service
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.service.device_service import DeviceService
from app.service.event_service import EventService
from app.service.notification_service import NotificationService

rabbitmq_broker = get_rabbitmq()
dramatiq.set_broker(rabbitmq_broker)

event_service: EventService = get_event_service()
device_service: DeviceService = get_device_service()
notification_service: NotificationService = get_notification_service()


@dramatiq.actor
def power_state_update(update_event: dict[str, str | float]):
    try:
        event_model = PowerStateUpdateEvent(**update_event)
    except ValueError as e:
        logging.exception(str(e))
        return

    device = device_service.device_exists(event_model.device_id)
    if device is None or not bool(device.active):
        return

    model = event_service.create_new_event(device.id, event_model)
    if model is None:
        return

    notification_service.send_notification(model)
