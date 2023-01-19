import csv, json, datetime

from utils.CollectionWebsite import CollectionWebsite, CollectionWebsiteEncoder
from utils.Creator import Creator, CreatorEncoder
from utils.Tools import Tools, ToolsEncoder
from utils.TradingDetails import TradingDetails, TradingDetailsEncoder
from utils.TrustWorthiness import TrustWorthiness, TrustWorthinessEncoder

class Collection:
	data = []

	def __init__(self, in_file: str=r"input/Rarity.csv"):
		with open(in_file, 'r', encoding='utf-8', newline='') as csv_file:
			csvReader = csv.DictReader(csv_file)
			
			for r in csvReader:
				data: dict = {}
				
				trust_worthiness = TrustWorthiness(0.01, 0.02)
				collection_website = CollectionWebsite(url=None, registered=None, registered_to=None, image_url=None)
				tools = Tools(rarity=None, open_sea=None, binance=None, rarible=None)				
				creator = Creator(name=None, sm=None, phones=None, emails=None, projects=None)

				data["name"] = r["Collection"]
				data["items"]: int = 9999
				data["id"]: int = 1234
				data["created"]: datetime = None
				data["updated"]: datetime = None
				data["discovered"]: datetime = None

				## These details are read from Rarity.csv as of now
				trading_details = TradingDetails(
					volume_7d = {"value": r["Volume (7d)"].split()[0], "CCY": r["Volume (7d)"].split()[1]},
					sales_7d = r["Sales (7d)"],
					volume_alltime = {"value": r["Volume (All Time)"].split()[0], "CCY": r["Volume (All Time)"].split()[1]},
					sales_alltime = r["Sales (All Time)"],
					avg_price_7d = {"value": r["Avg Price (7d)"].split()[0], "CCY": r["Avg Price (7d)"].split()[1]},
					total_supply = r["Total Supply"],
					owners = r["Owners"],
					owners_percent = r["Owners%"],
					estimated_market_cap = {"value": r["Estimated Market Cap"].split()[0], "CCY": r["Estimated Market Cap"].split()[1]},
					added = r["Added"]
				)

				data["trust_worthiness"] = TrustWorthinessEncoder().encode(trust_worthiness)
				data["collection_website"] = CollectionWebsiteEncoder().encode(collection_website)
				data["tools"] = ToolsEncoder().encode(tools)
				data["creator"] = CreatorEncoder().encode(creator)
				data["trading_details"] = TradingDetailsEncoder().encode(trading_details)

				self.data.append(data)

	def create(self, out_file: str=r"output/Rarity.json"):
		with open(out_file, 'w', encoding='utf-8') as json_file:
			json_file.write(json.dumps(self.data, indent=4, ensure_ascii=False))
