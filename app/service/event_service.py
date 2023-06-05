import uuid

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.event_model import EventModel
from app.model.event.power_state_update import PowerStateUpdateEvent
from app.redis.redis_client import RedisClient


class EventService:
    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def create_new_event(self, event: PowerStateUpdateEvent) -> None:
        try:
            model = EventModel(device_id=event.device_id,
                               power_state=event.power_state,
                               network_level=event.network_level,
                               battery_level=event.battery_level,
                               created_at=event.fired_at,
                               updated_at=event.fired_at)
            self.firebase_client.client.collection('Events').document(str(uuid.uuid4())).set(model.to_dict())
        except Exception as e:
            print(e)
