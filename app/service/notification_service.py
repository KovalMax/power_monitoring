from app.firebase.firebase_client import FireBaseClient
from app.model.domain.models import EventModel
from app.redis.redis_client import RedisClient


class NotificationService:
    POWER_STATE_CACHE_PREFIX = 'events:state'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def send_notification(self, model: EventModel):
        state_key = self.__get_key(model.device_id)
        state_entry = self.redis_client.get(state_key)
        if state_entry is None:
            self.redis_client.set(state_key, model.power_state.value)
            return

        if int(state_entry) != model.power_state.value:
            pass

    def __get_key(self, key_value: str) -> str:
        return f'{self.POWER_STATE_CACHE_PREFIX}:{key_value}'
