import operator
from os import environ

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import FieldFilter
from google.cloud.firestore_v1.types import StructuredQuery

from app.redis.redis_client import get_key, set_key

cred = credentials.Certificate(environ.get('FIREBASE_KEY'))
default_app = firebase_admin.initialize_app(cred)
db: firestore.firestore.Client = firestore.client()


def device_exists(device_id: str) -> bool:
    if get_key(device_id):
        return True

    device_filter = FieldFilter('device_id', StructuredQuery.FieldFilter.Operator.EQUAL.value, device_id)
    query = db.collection('Devices').where(filter=device_filter).limit(1)
    snapshot = query.stream()

    exists = sum(1 for _ in snapshot) > 0
    if exists:
        set_key(device_id, True)

    return exists
