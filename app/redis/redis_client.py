from typing import Any

import redis


class RedisClient:
    def __init__(self, client: redis.Redis):
        self.redis = client

    def get(self, key: str) -> Any | None:
        return self.redis.get(key)

    def set(self, key: str, value: Any):
        return self.redis.set(key, value)

    def hget(self, key: str) -> dict:
        return self.redis.hgetall(key)

    def hset(self, key: str, value: dict):
        return self.redis.hset(key, mapping=value)
