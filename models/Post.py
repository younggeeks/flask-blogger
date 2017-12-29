import uuid
from datetime import datetime

from Model import Model


class Post(Model):
    collection = "posts"

    def __init__(self, title, body, user_id, category):
        Model.__init__(self, collection=self.collection)
        self.title = str(title),
        self.body = body,
        self.published_at = str(datetime.utcnow())
        self.user_id = user_id,
        self.category = category
        self.id = uuid.uuid4().hex

    def json(self):
        return {
            "title": self.title,
            "body": self.body,
            "published_at": self.published_at,
            "category": self.category,
            "id": self.id
        }
