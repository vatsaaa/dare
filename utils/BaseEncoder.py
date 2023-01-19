from json import JSONEncoder

class BaseEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
