import FireStorage
from Firestore import Firestore


class Model:
    def __init__(self, collection):
        self.collection = collection

    @classmethod
    def all(cls):
        return Firestore.fetch_all(cls.collection)

    @classmethod
    def get_one(cls, id):
        return Firestore.fetch_one(collection=cls.collection, id=id)

    @classmethod
    def get(cls, query):
        return Firestore.fetch_by(collection=cls.collection, query=query)

    @classmethod
    def save(cls, data, resource_id=None, cover=None):
        if cover:
            print("the file from up here is ", cover)
            cls.upload(cover=cover, id=data["id"])
        results = Firestore.save(cls.collection, data=data, id=resource_id)
        return results

    @classmethod
    def upload(cls, cover, id):
        # TODO move upload logic to here for reusability
        print("from down here it looks like ", cover)
        FireStorage.upload_file(file=cover, id=id)



