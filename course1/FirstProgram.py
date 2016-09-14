fname = raw_input('enter file name : ')
if len(fname) == 0 :
	fname = 'mbox-short.txt'
fh = open(fname)
result=dict()
for line in fh:
	if not line.startswith('From'):
		continue
	if line.startswith('From:'):
		continue
	line=line.rstrip()
	words=line.split()
	time=words[5].split(':')
	result[time[0]]=result.get(time[0],0)+1
tmp=result.items()
tmp.sort()
for v,k in tmp:
	print v,k