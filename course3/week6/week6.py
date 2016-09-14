import json
import urllib

url = raw_input('Enter URL ')
data = urllib.urlopen(url).read()

info = json.loads(data)
lst = info['comments']
sum=0
for item in lst:
	sum=sum+item["count"]
print sum	