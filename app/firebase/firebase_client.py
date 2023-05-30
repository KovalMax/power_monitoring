import uuid
from os import environ

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import FieldFilter

from app.model.domain.event_model import EventModel
from app.redis.redis_client import get_device, set_new_device

cred = credentials.Certificate(environ.get('FIREBASE_KEY'))
default_app = firebase_admin.initialize_app(cred)
db: firestore.firestore.Client = firestore.client()


def device_exists(device_id: str) -> bool:
    if get_device(device_id):
        return True

    device_filter = FieldFilter('device_id', '==', device_id)
    query = db.collection('Devices').where(filter=device_filter).limit(1)
    snapshot = query.stream()

    exists = sum(1 for _ in snapshot) > 0
    if exists:
        set_new_device(device_id)

    return exists


def create_new_event(event: EventModel) -> None:
    db.collection('Events').document(str(uuid.uuid4())).set(event.to_dict())
