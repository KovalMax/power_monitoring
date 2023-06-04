from firebase_admin import credentials, firestore, initialize_app as firebase_init_app
from firebase_admin.firestore import firestore as firestore_admin_client


class FireBaseClient:
    def __init__(self, path_to_firebase_key: str):
        cred = credentials.Certificate(path_to_firebase_key)
        firebase_init_app(cred)

        self.client: firestore_admin_client.Client = firestore.client()
