import logging
import uuid

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.event_model import EventModel
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.redis.redis_client import RedisClient


class EventService:
    DEVICE_COLLECTION = 'Devices'
    EVENT_COLLECTION = 'events'
    POWER_STATE_CACHE_PREFIX = 'events:state'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def create_new_event(self, event: PowerStateUpdateEvent) -> None:
        try:
            model = EventModel(device_id=event.device_id,
                               power_state=event.power_state,
                               network_level=event.network_level,
                               battery_level=event.battery_level,
                               created_at=event.fired_at)

            collection = self.firebase_client.client.collection(self.EVENT_COLLECTION)
            collection.document(str(uuid.uuid4())).set(model.to_dict())

            state_key = self.__get_key(model.device_id)
            state_entry = self.redis_client.get(state_key)
            if state_entry is None:
                self.redis_client.set(state_key, model.power_state.value)
                return

            if int(state_entry) != model.power_state.value:
                pass
        except ValueError as e:
            logging.exception(str(e))

    def __get_key(self, key_value: str) -> str:
        return f'{self.POWER_STATE_CACHE_PREFIX}:{key_value}'
