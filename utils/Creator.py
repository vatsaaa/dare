from json import JSONEncoder

from utils.Presence import Presence

class Creator:
    presence = {}

    def __init__(self, name: str, sm: list, phones: list, emails: list, projects: list):
        self.name = name
        self.presence = Presence(sm, phones, emails)
        self.projects = projects

class CreatorEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
