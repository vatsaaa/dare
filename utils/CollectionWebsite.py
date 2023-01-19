import datetime
from json import JSONEncoder

class CollectionWebsite:
    def __init__(self, url: str, registered: datetime, registered_to: str, image_url: str):
        self.url = url
        self.registered = registered
        self.registered_to = registered_to
        self.image_url = image_url

class CollectionWebsiteEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
