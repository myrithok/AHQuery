from ah import Auction
from ah import AuctionHouse

def getConfig(item):
	file = "config"
	f = open(file,"r")
	contents = f.read().splitlines()
	f.close()
	for l in contents:
		if l.startswith(item):
			return l.split('=')[1]
	return "Not Found"

def loadAH(crid):
	file = crid
	f = open(file,"r")
	contents = f.read().splitlines()
	f.close()
	ah = AuctionHouse()
	for l in contents:
		a = Auction(l)
		ah.add(a)
	return ah