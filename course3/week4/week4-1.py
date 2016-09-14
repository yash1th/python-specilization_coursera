import urllib
from BeautifulSoup import *
url = raw_input('Enter url - ')
count = int(raw_input('Enter count - '))
position = int(raw_input('Enter position - '))

html = urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup('a')
while count>1:
	tag = tags[position-1]
	print tag.contents[0]
	url = tag.get('href', None)
	html = urllib.urlopen(url).read()
	soup=BeautifulSoup(html)
	tags=soup('a')
	count=count-1
print tags[position-1].contents[0]

#http://python-data.dr-chuck.net/known_by_Basher.html , count = 7, position = 18, Elice

#http://python-data.dr-chuck.net/known_by_Fikret.html
#count = 4, position 3, Anayah
#Fikret count=4
#Montgomery count=3
#Mhairade count=2
#Butchi count=1, exits the loop but before that the current url,htm,soup,tags contains the page containing the answer 
#Anayah