import datetime
from json import JSONEncoder

class SocialMedia:
    def __init__(self, sm_name: str, handle: str, since: datetime, friends: int, followers: int):
        self.name = sm_name
        self.handle = handle
        self.since = since
        self.friends = friends
        self.followers = followers

class SocialMediaEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
