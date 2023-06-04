from typing import Any

import redis


class RedisClient:
    def __init__(self, host: str, port: str, db: str):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def get(self, key: str) -> Any | None:
        return self.redis.get(key)

    def set(self, key: str, value: Any):
        return self.redis.set(key, value)
