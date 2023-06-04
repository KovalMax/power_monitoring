import uuid

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.event_model import EventModel
from app.redis.redis_client import RedisClient


class EventService:
    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def create_new_event(self, event: EventModel) -> None:
        self.firebase_client.client.collection('Events').document(str(uuid.uuid4())).set(event.to_dict())
