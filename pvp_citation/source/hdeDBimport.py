import re, time
import mysql.connector
from datetime import datetime
t_start = time.time()

file = open('hde01_ADD.txt','r')
content = file.read()
file.close()

resultd,result,date,res  = {},[],[],[]
b = re.compile('(<I>[^<\(]* v. [^<]*</I>)[^\s]*\s+\[\s+([^\]]+)\][^\(]*\([^)]+\s+([1-2][0-9][0-9][0-9])\)', re.IGNORECASE)
#rep = {"condition1": "", "condition2": "text"}
#b = re.compile('(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[\s+[^\]]+\])', re.MULTILINE)
#(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[[^\]]+\])
#((&lsqb;|\[)[^\[]*(&rsqb;|\]))
#a = re.compile('<I>([^<]* v. [^<]*)</I>')
c = re.compile('<I>([^<]+)</I>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)

result1 = b.findall(content)
#DB = dict(result1)

for each in result1:
    if int(each[2])>=1995:
        date.append(each)
		
for every in date:
    a = every[0].replace("\n"," ").replace('See ','').replace('e.g., ','').replace('Pages- ','').replace('cf. ','').replace('e.g. ','').replace('f. ','').replace('cf. ','').replace('citing ','').replace('.&rdquo ','').replace('Id.; ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','').replace('<I> ','<I>')
    b = every[1].replace("\n","").replace("[<","[ <").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
    q = c.findall(a)
    unq = ''.join(d.findall(q[0]))
	  #a = re.compile('\s\s+'," ")
    #b = re.compile('\s\s+'," ")
    result.append((unq,(a,b,every[2])))
	
#print(len(result))

#.replace('see ','').replace('e.g., ','').replace('See, ','').replace('See ','').replace('But ','').replace('see, ','').replace('also ','')
resultd = dict(result)
#print(result, " \nin ", time.time() - t_start,"s")
#print(len(resultd))
#print(result)

#connect to the server
cnx = mysql.connector.connect(user='root', password='aloysius', host='localhost', database='citation')
cursor = cnx.cursor()

t = datetime.date(datetime.now())
add = ("INSERT INTO `cite` (`USER`, `DATE`, `PRODUCT`, `PVP`, `LINK`, `UNQ`, `YEAR`, `STATUS`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

for key in resultd:
	value = resultd[key]
	val0 = value[0]
	val1 = value[1].replace('"','\"')
	val2 = value[2]
	#.append((key,val1,val2,unq))
	data = ('MASTER',t,'HDE',val0,val1,key,val2,'DONE')
	# Insert new record
	cursor.execute(add, data)
	cnx.commit()
cursor.close
	
#print(resultd)
print(time.time()-t_start)	

cnx.close()
	

'''
	query = ("SELECT `ID`, `USER`, `DATE`, `PVP`, `LINK`, `UNQ`, `YEAR`, `STATUS` FROM `cite` WHERE `ID`= 8000")
	row = cursor.fetchone()
	while row is not None:
		print(row)
		row = cursor.fetchone()

	cursor.execute(query)
	
	for some in cursor:
	  print(some)	
'''	  
'''with open("opb.txt", "w") as file:
	for key in res:
		
		file.write(key[0] + "\t"+ str(key[1])  + "\n")
	file.close()
'''	
'''
with open("test.txt", "w") as myfile:
    for key in resultd:
            myfile.write(resultd[key] + "\n")
    myfile.close()
#print(resultd['<I>Southard v. Texas Board of Criminal Justice</I>'], " \nin ", time.time() - t_start,"s")
'''