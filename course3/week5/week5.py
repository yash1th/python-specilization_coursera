import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL - ')
data = urllib.urlopen(url).read()

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print 'total count: ',len(lst)
sum=0
for item in lst:
	sum=sum+int(item.find('count').text)
print sum	
