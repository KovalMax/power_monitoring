from functools import lru_cache
from os import environ

import firebase_admin
import redis
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from firebase_admin import credentials, firestore

from app.firebase.firebase_client import FireBaseClient
from app.redis.redis_client import RedisClient
from app.service.device_service import DeviceService
from app.service.event_service import EventService

mq = RabbitmqBroker(url=environ.get("BROKER_HOST"))
redis = redis.Redis(host=environ.get("REDIS_HOST"), port=environ.get("REDIS_PORT"), db=environ.get("REDIS_INDEX"))
cred = credentials.Certificate(environ.get("FIREBASE_KEY"))
default_app = firebase_admin.initialize_app(cred)
firestore = firestore.client()


def get_redis_client() -> RedisClient:
    return RedisClient(redis)


def get_firebase_client() -> FireBaseClient:
    return FireBaseClient(firestore)


@lru_cache(typed=True)
def get_rabbitmq() -> RabbitmqBroker:
    return mq


def get_event_service() -> EventService:
    return EventService(get_redis_client(), get_firebase_client())


def get_device_service() -> DeviceService:
    return DeviceService(get_redis_client(), get_firebase_client())
