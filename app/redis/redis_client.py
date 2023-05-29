from os import environ

import redis

redis = redis.Redis(host=environ.get("REDIS_HOST"), port=environ.get("REDIS_PORT"), db=environ.get("REDIS_INDEX"))


def get_device(device_id: str) -> bool | None:
    return redis.get(f'devices:${device_id}')


def set_new_device(device_id: str, value: bool = True):
    return redis.set(f'devices:${device_id}', value)
