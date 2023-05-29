from os import environ

import redis

redis = redis.Redis(host=environ.get("REDIS_HOST"), port=environ.get("REDIS_PORT"), db=environ.get("REDIS_INDEX"))


def get_key(key: str):
    return redis.get(key)


def set_key(key: str, value: bool):
    return redis.set(key, value)
