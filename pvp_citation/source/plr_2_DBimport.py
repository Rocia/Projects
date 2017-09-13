import re, time
import mysql.connector
from datetime import datetime
t_start = time.time()

t_start = time.time()

file = open('plr01.txt','r')
content = file.read()
file.close()

resultd,result,date = {},[],[]
b = re.compile('(<ITALIC>[^<]+v.[^<]+</ITALIC>)[^\[<]*\[\n<SMALL-CAP>[^<]+</SMALL-CAP>\s+\n(<XREF[^<]+</XREF>)\][^(]+\([^)]+\s+([1-2][0-9][0-9][0-9])\)', re.MULTILINE)
c = re.compile('<ITALIC>([^<]+)</ITALIC>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)


result1 = b.findall(content)
#DB = dict(result1)
'''for each in result1:
    if int(each[2])>=1995:
        date.append(each)'''
for every in result1:
#    new = every[:2]
    a = every[0].replace("\n"," ")
    b = every[1].replace("\n","").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
    q = c.findall(a)
    unq = ''.join(d.findall(q[0]))
    result.append((unq,(a,b)))
#result.append((a,b))

resultd = dict(result)
#print(resultd, " \nin ", time.time() - t_start,"s")


cnx = mysql.connector.connect(user='root', password='aloysius', host='localhost', database='citation')
cursor = cnx.cursor()

t = datetime.date(datetime.now())
add = ("INSERT INTO `cite` (`USER`, `DATE`, `PRODUCT`, `PVP`, `LINK`, `UNQ`, `STATUS`) VALUES (%s, %s, %s, %s, %s, %s, %s)")

for key in resultd:
	value = resultd[key]
	pvp = value[0].replace('ITALIC','I')
	link = value[1].replace('"','\"')
	#.append((key,val1,val2,unq))
	data = ('MASTER',t,'PLR',pvp,link,key,'DONE')
	# Insert new record
	cursor.execute(add, data)
	cnx.commit()
cursor.close
	
#print(resultd)
print(time.time()-t_start)	

cnx.close()
'''with open("PLR.txt", "w") as myfile:
    for key in resultd:
            myfile.write(key + "\t"+ (resultd[key]) + "\n")
    myfile.close()
    
with open("test.txt", "w") as myfile:
    for key in resultd:
            myfile.write(resultd[key] + "\n")
    myfile.close()
'''	
#print(resultd['<I>Southard v. Texas Board of Criminal Justice</I>'], " \nin ", time.time() - t_start,"s")
