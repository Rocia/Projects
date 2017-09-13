import re, time

t_start = time.time()

file = open('b.txt','r')
content = file.read()
file.close()

resultd,result,date,Result,listt  = {},[],[],[],[]
b = re.compile('(<I>[^<\(]* v. [^<]*</I>)[^\s]*\s+\[\s+([^\]]+)\][^\(]*\([^)]+\s+([1-2][0-9][0-9][0-9])\)', re.IGNORECASE)
#rep = {"condition1": "", "condition2": "text"}
#b = re.compile('(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[\s+[^\]]+\])', re.MULTILINE)
#(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[[^\]]+\])
#((&lsqb;|\[)[^\[]*(&rsqb;|\]))
#a = re.compile('<I>([^<]* v. [^<]*)</I>')
result1 = b.findall(content)
#DB = dict(result1)

c = re.compile('<I>([^<]+)</I>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)

for each in result1:
    if int(each[2])>=1995:
        date.append(each)
		
for every in date:
    a = every[0].replace("\n"," ").replace('See ','').replace('e.g., ','').replace('Pages- ','').replace('cf. ','').replace('e.g. ','').replace('f. ','').replace('cf. ','').replace('citing ','').replace('.&rdquo ','').replace('Id.; ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','').replace('<I> ','<I>')
    b = every[1].replace("\n","").replace("[<","[ <").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
    #a = re.compile('\s\s+'," ")
    #b = re.compile('\s\s+'," ")
    result.append((a,(b,every[2])))
	
#print(len(result))

#.replace('see ','').replace('e.g., ','').replace('See, ','').replace('See ','').replace('But ','').replace('see, ','').replace('also ','')
resultd = dict(result)
#print(result, " \nin ", time.time() - t_start,"s")
#print(len(resultd))
#print(result)
for key in resultd:
	Result.append((key.replace('also, ','').replace('e.g., ','').replace('cf. ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('But ','').replace('generally ','').replace('compare ',''),resultd[key]))
	
#print(res[0])
for res in Result:
	k = res[0]
	unq= c.findall(k)
	uk= ''.join(d.findall(unq[0]))
	i = res[1]
	v = i[0]
	yr = i[1]
	listt.append((k,v,uk,yr))
		


with open("opb.txt", "w") as file:
	for key in listt:
		file.write('("MASTER010708","'+key[0] +'",'+"'"+ key[1] +"','"+ key[2]+"','"+ key[3] +"')\n")
	file.close()

'''
with open("test.txt", "w") as myfile:
    for key in resultd:
            myfile.write(resultd[key] + "\n")
    myfile.close()
#print(resultd['<I>Southard v. Texas Board of Criminal Justice</I>'], " \nin ", time.time() - t_start,"s")
'''