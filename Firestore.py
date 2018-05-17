from google.cloud import firestore, exceptions

db = firestore.Client()

posts_ref = db.collection(u'posts')


class Firestore:
    @staticmethod
    def fetch_all(collection):
        try:
            cursor = db.collection(collection).get()
            return cursor
        except exceptions.NotFound as e:
            return e

    @staticmethod
    def fetch_one(collection, id):
        try:
            cursor = db.collection(collection).document(id).get()
            return cursor
        except exceptions.NotFound as e:
            return e

    @staticmethod
    def fetch_by(collection, query=None):
        kweri = db.collection(collection)
        if not query:
            return kweri.get()
        else:
            for q, val in query.items():
                kweri.where(q, '==', val)

        return kweri.get()

    @staticmethod
    def save(collection, data, id=None):
        if id:
            return db.collection(collection).document(id).update(data)
        else:
            return db.collection(collection).document(data.get("id")).set(data)
