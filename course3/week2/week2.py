import re

fh = open('regex_sum_42.txt')
fi = fh.read()
res = re.findall('[0-9]+',fi)
sum=0
for element in res:
	sum=sum+int(element)
print sum

