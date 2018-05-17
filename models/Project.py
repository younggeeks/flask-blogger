import uuid

from Model import Model


class Project(Model):
    collection = "projects"

    def __init__(self, title, description, start, owner, technologies, status, role, image, url):
        self.title = title
        self.owner = owner
        self.description = description
        self.start = start
        self.technologies = technologies
        self.status = status
        self.role = role
        self.image = image
        self.url = url
        self.id = uuid.uuid4().hex

    def json(self):
        return {
            "title": self.title,
            "owner": self.owner,
            "start": self.start,
            "technologies": self.technologies,
            "status": self.status,
            "role": self.role,
            "url": self.url,
            "id": self.id
        }
