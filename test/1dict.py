import re, time

t_start = time.time()
with open('opb.txt') as f:
	lines = f.readlines()
f.close()
LIST,LIST2,result=[],[],[]

a = re.compile('(<I>[^<]+</I>)', re.IGNORECASE)
b = re.compile('(<XREF[^>]*>[^<]+</XREF>)', re.IGNORECASE)
c = re.compile('<I>([^<]+)</I>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)
e = re.compile("([1-2][\d+][\d+][\d+])",re.IGNORECASE)

#print(lines[0])
for line in lines:
	#print(line)
	key = a.findall(line)
	k = key[0].replace('also, ','').replace('e.g., ','').replace('cf. ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','')
	value = b.findall(line)
	unq = c.findall(k)
	unqkey = ''.join(d.findall(unq[0]))
	date = e.findall(line)
	res = (k,value[0].replace("'","''"),unqkey,date[0])
	#print(res)
	result.append(res)

with open ('report_hed01.txt','w') as f:
	for item in result:
		f.write('("MASTER010708","'+item[0]+'",'+"'"+item[1]+"','"+item[2]+"','"+item[3]+"')\n")
	f.close()
	