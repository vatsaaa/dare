from json import JSONEncoder

class TrustWorthiness:
    def __init__(self, dare: float, user: float):
        self.dare = dare
        self.user = user

class TrustWorthinessEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
