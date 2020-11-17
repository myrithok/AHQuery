from util import getConfig
from util import loadAH
from ah import Auction
from ah import AuctionHouse
from api import getItemId

items = ["tidespray linen"]
itemcosts = {}
apikey = getConfig('apikey')
crid = "1171"
ah = loadAH(crid)
for item in items:
	ii = getItemId(item,apikey)
	print(ii)
	i = ah.getItem(ii)
	c = set()
	for a in i:
		c.add(a.cost)
	print(c)
	itemcosts[item] = min(c)
print(itemcosts)