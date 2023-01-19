from json import JSONEncoder

class Tools:
    def __init__(self, rarity: str, open_sea: str, binance: str, rarible: str):
        self.rarity = rarity
        self.open_sea = open_sea
        self.binance = binance
        self.rarible = rarible

class ToolsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
