from os import environ

import firebase_admin
from firebase_admin import credentials, firestore
from app.redis.redis_client import get_key, set_key

cred = credentials.Certificate(environ.get('FIREBASE_KEY'))
default_app = firebase_admin.initialize_app(cred)
db: firestore.firestore.Client = firestore.client()


def device_exists(device_id: str) -> bool:
    if get_key(device_id):
        return True

    query = db.collection('Devices').where('device_id', '==', device_id).limit(1)
    snapshot = query.stream()
    exists = len(snapshot) > 0

    if exists:
        set_key(device_id, True)

    return exists
