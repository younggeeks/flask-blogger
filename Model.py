from Firestore import Firestore


class Model:
    def __init__(self, collection):
        self.collection = collection

    @classmethod
    def all(cls):
        return Firestore.fetch_all(cls.collection)

    @classmethod
    def get_one(cls, post_id):
        return Firestore.fetch_one(collection=cls.collection, id=post_id)

    @classmethod
    def get(cls, query):
        return Firestore.fetch_by(collection=cls.collection, query=query)

    @classmethod
    def save(cls, data, post_id=None):
        return Firestore.save(cls.collection, data=data, post_id=post_id)
