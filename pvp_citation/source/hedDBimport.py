import re, time
#import MySQLdb

t_start = time.time()

def readfile (filename):
	file = open(filename+'.xml','r')
	content = file.read()
	file.close()
	return content

resultd,result,date,res  = {},[],[],[]
b = re.compile('(<I>[^<\(]* v. [^<]*</I>)', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)

cont = readfile("15954")
result = b.findall(cont)

for each in result:
	 a = each.replace("\n"," ").replace('See ','').replace('e.g., ','').replace('Pages- ','').replace('cf. ','').replace('e.g. ','').replace('f. ','').replace('cf. ','').replace('citing ','').replace('.&rdquo ','').replace('Id.; ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','').replace('<I> ','<I>')
	 res.append(a)
	 
print(res)
	 
