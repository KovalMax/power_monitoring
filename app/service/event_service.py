import logging
import uuid

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.models import EventModel
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.redis.redis_client import RedisClient


class EventService:
    DEVICE_COLLECTION = 'Devices'
    EVENT_COLLECTION = 'events'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def create_new_event(self, device_reference: str, event: PowerStateUpdateEvent) -> EventModel | None:
        try:
            model = EventModel(device_id=event.device_id,
                               power_state=event.power_state,
                               network_level=event.network_level,
                               battery_level=event.battery_level,
                               created_at=event.fired_at)

            device = self.firebase_client.client.collection(self.DEVICE_COLLECTION).document(device_reference)
            device.collection(self.EVENT_COLLECTION).add(model.to_dict(), str(uuid.uuid4()))

            return model
        except ValueError as e:
            logging.exception(str(e))
            return None
