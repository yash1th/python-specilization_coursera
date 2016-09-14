import urllib
import json

serviceurl='http://python-data.dr-chuck.net/geojson?'
address = raw_input('enter location : ')
if len(address)<=0:
	address='The University of Latvia'
url = serviceurl + urllib.urlencode({'sensor':'false','address':address})
print url
data = urllib.urlopen(url).read()
js=json.loads(str(data))

place_id=js["results"][0]["place_id"]
print place_id
#The University of Latvia