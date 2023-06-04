from os import environ

from dramatiq.brokers.rabbitmq import RabbitmqBroker

from app.firebase.firebase_client import FireBaseClient
from app.redis.redis_client import RedisClient
from app.service.device_service import DeviceService
from app.service.event_service import EventService


def get_redis_client() -> RedisClient:
    return RedisClient(environ.get("REDIS_HOST"), environ.get("REDIS_PORT"), environ.get("REDIS_INDEX"))


def get_firebase_client() -> FireBaseClient:
    return FireBaseClient(environ.get("FIREBASE_KEY"))


def get_rabbitmq() -> RabbitmqBroker:
    return RabbitmqBroker(url=environ.get("BROKER_HOST"))


def get_event_service(redis_client: RedisClient = get_redis_client(),
                      firebase_client: FireBaseClient = get_firebase_client()) -> EventService:
    return EventService(redis_client, firebase_client)


def get_device_service(redis_client: RedisClient = get_redis_client(),
                       firebase_client: FireBaseClient = get_firebase_client()) -> DeviceService:
    return DeviceService(redis_client, firebase_client)

