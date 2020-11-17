from api import getAuctionData
from api import getConnectedRealmId
from util import getConfig

apikey = getConfig('apikey')
realm = getConfig('realm')

crid = getConnectedRealmId(realm,apikey)
results = getAuctionData(crid,apikey)
file = crid
f = open(file,"w")
for a in results['auctions']:
	f.write(str(a) + "\n")
f.close()