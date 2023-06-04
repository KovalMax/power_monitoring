from firebase_admin.firestore import firestore


class FireBaseClient:
    def __init__(self, client: firestore.Client):
        self.client = client
