import requests

def getAuctionData(crid,apikey):
	url = 'https://us.api.blizzard.com/data/wow/connected-realm/' + crid + '/auctions?namespace=dynamic-us&locale=en_US&access_token=' + apikey
	results = requests.get(url).json()
	return results

def getRealmSlug(name,apikey):
	url = 'https://us.api.blizzard.com/data/wow/realm/index?namespace=dynamic-us&locale=en_US&access_token=' + apikey
	results = requests.get(url).json()
	for r in results['realms']:
		if r['name'] == name:
			return r['slug']
	return "Not Found"

def getConnectedRealmId(name,apikey):
	slug = getRealmSlug(name,apikey)
	url = 'https://us.api.blizzard.com/data/wow/realm/' + slug + '?namespace=dynamic-us&locale=en_US&access_token=' + apikey
	results = requests.get(url).json()
	crid = results['connected_realm']['href'][53:].split('?')[0]
	return crid

def getItemId(name,apikey):
	url = 'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&locale=en_US&name.en_US=' + name.replace(" ","%20") + '&orderby=id&_page=1&access_token=' + apikey
	results = requests.get(url).json()
	for r in results['results']:
		if r['data']['name']['en_US'].lower() == name.lower():
			return r['data']['id']
	return "Not Found"