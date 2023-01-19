from json import JSONEncoder

class Presence:
    sm = []

    def __init__(self, sm: list, phones: list, emails: list):
        self.sm = sm
        self.others = {"phones": phones, "emails": emails}

class PresenceEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
