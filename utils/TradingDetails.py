from json import JSONEncoder

class TradingDetails:
    def __init__(self, volume_7d: dict, sales_7d: str, volume_alltime: dict, sales_alltime: str, avg_price_7d: dict, total_supply, owners, owners_percent, estimated_market_cap: dict, added):
        self.volume_7d = volume_7d
        self.sales_7d = sales_7d
        self.volume_alltime = volume_alltime
        self.sales_alltime = sales_alltime
        self.avg_price_7d = avg_price_7d
        self.total_supply = total_supply
        self.owners = owners
        self.owners_percent = owners_percent
        self.estimated_market_cap = estimated_market_cap
        self.added = added
        
class TradingDetailsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
