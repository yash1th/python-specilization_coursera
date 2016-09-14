fname = raw_input('enter file name ')
if len(fname)<=1:
    fname='mbox.txt'
fh = open(fname)
org = dict()
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    words = line.split()
    email = words[1].split('@')
    host = email[1]
    org[host]=org.get(host,0)+1
