class AuctionHouse:
	def __init__(self):
		self.auctions = set()
	def add(self,auction):
		self.auctions.add(auction)
	def getItem(self,item):
		results = set()
		for a in self.auctions:
			if a.item == item:
				results.add(a)
		return results

class Auction:
	def __init__(self,raw):
		contents = raw[1:-1].split(",")
		self.id = ""
		self.item = 0
		self.cost = 0
		self.quantity = 0
		for l in contents:
			if l.startswith("'id': "):
				self.id = l[6:]
			elif l.startswith(" 'item': {'id': "):
				self.item = int(l[16:].replace(",","").replace("}","").strip())
			elif l.startswith(" 'unit_price': "):
				self.cost = int(l[15:])
			elif l.startswith(" 'buyout': "):
				self.cost = int(l[11:])
			elif l.startswith(" 'quantity': "):
				self.quantity = int(l[13:])