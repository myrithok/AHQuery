from api import getRealmSlug
from util import getConfig

realm = getConfig('realm')
apikey = getConfig('apikey')

a = getRealmSlug(realm,apikey)
print(a)