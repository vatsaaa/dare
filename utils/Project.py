from json import JSONEncoder

class Project:
    def __init__(self, name, id, collection_website):
        self.name = name
        self.id = id
        self.collection_website = collection_website

class ProjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
