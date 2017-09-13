import re


def readdata(filename):
	file = open(filename+'.xml','r+')
	content = file.read()
	file.close()
	#findi(content)
	result = a.findall(content)
	return result

def readdict(productname):
	with open(productname+'.txt') as f:
		lines = f.read().splitlines()
	f.close()
	return lines

def updatefile(filename,k,v):
	with open(filename+'.xml','r+') as f:
		content = f.read()
		update = content.replace(k,k+' '+v)
		f.write(update)
		f.close()
	
	
def unmatched(k):
	with open('UNMATCHED.txt') as File:
		File.write(k + "\n")
	File.close()
		
		
def updatedict(k,v):
	with open('UNMATCHED.txt') as f:
		f.write(k+'\t'+v+'\t'+''.join(d.findall(item)))
		f.close()
		
		
UNQLIST,KVP,matches,LIST,unmatch= [],[],{},[],{}
a = re.compile('<I>([^<]+v.[^<]+)</I>', re.IGNORECASE)
b = re.compile('</XREF>([^<]+)', re.IGNORECASE)
c = re.compile('(<XREF[^>]*>[^<]+</XREF>)', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)
#print(readdata(file))

PVP = readdata('15954')
for item in PVP:
	data = ''.join(d.findall(item))
	data1= data.replace('See','').replace('see','').replace('also','').replace('etc.,','')
	UNQLIST.append((item.replace('See','').replace('see',''),data1))
	LIST.append(data1)

#print(UNQLIST)
	
dictionary = readdict('report_hde01')
#print(dictionary)

for item in dictionary:
	key = b.findall(item)
	unqkey = key[0].replace('\t','')
	value = c.findall(item)
	#unqkey = ''.join(d.findall(key[0]))
	KVP.append((unqkey,value[0]))##
	
DICT = dict(KVP)
#print(DICT)

'''for i in UNQLIST:
	if i[1] in DICT:
		key = UNQLIST[0]
		matches[key] = DICT[key]
		updatefile('15954',key,matches[key])
	else:
		unmatched(i[0])
'''