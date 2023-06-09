from google.cloud.firestore_v1 import FieldFilter

from app.firebase.firebase_client import FireBaseClient
from app.model.domain.models import DeviceModel
from app.redis.redis_client import RedisClient


class DeviceService:
    DEVICE_CACHE_PREFIX = 'map:devices'
    COLLECTION_NAME = 'Devices'
    DEVICE_ID_FIELD = 'deviceId'

    def __init__(self, redis_client: RedisClient, firebase_client: FireBaseClient):
        self.redis_client = redis_client
        self.firebase_client = firebase_client

    def device_exists(self, device_id: str) -> DeviceModel | None:
        cache_key = self.__get_key(device_id)
        redis_entry = self.redis_client.hget(cache_key)
        #if len(redis_entry) > 0:
         #   return DeviceModel(**redis_entry)

        device_filter = FieldFilter(self.DEVICE_ID_FIELD, '==', device_id)
        query = self.firebase_client.client.collection(self.COLLECTION_NAME).where(filter=device_filter).limit(1)
        snapshot = query.get()

        for device in snapshot:
            snapshot_dict = device.to_dict()
            device = DeviceModel(id=device.id,
                                 device_id=snapshot_dict[self.DEVICE_ID_FIELD],
                                 user_id=snapshot_dict['userId'],
                                 active=int(snapshot_dict['active']),
                                 name=snapshot_dict['deviceName'],
                                 location=snapshot_dict['deviceLocation'],
                                 )

            self.redis_client.hset(cache_key, device.to_dict())

            return device

        return None

    def __get_key(self, key_value: str) -> str:
        return f'{self.DEVICE_CACHE_PREFIX}:{key_value}'
