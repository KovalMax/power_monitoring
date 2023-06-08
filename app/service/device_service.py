from google.cloud.firestore_v1 import FieldFilter

from app.firebase.firebase_client import FireBaseClient
from app.redis.redis_client import RedisClient


class DeviceService:
    DEVICE_CACHE_PREFIX = 'app:devices'
    COLLECTION_NAME = 'Devices'
    DEVICE_ID_FIELD = 'deviceId'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def device_exists(self, device_id: str) -> bool:
        # cache_key = self.__get_key(device_id)
        # redis_entry = self.redis_client.get(cache_key)
        # if redis_entry is not None:
        #     return True

        device_filter = FieldFilter(self.DEVICE_ID_FIELD, '==', device_id)
        query = self.firebase_client.client.collection(self.COLLECTION_NAME).where(filter=device_filter).limit(1)
        snapshot = query.get()

        for device in snapshot:
            print(device.id)
            print(device.to_dict())

        return True

    def __get_key(self, key_value: str) -> str:
        return f'{self.DEVICE_CACHE_PREFIX}:{key_value}'
