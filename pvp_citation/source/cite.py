import re, time, sys
import  psycopg2
from datetime import datetime

class CustomError(Exception):
	pass

def readdata(filewithpath,phase):
	file = open(filewithpath,'r+')
	content = file.read()
	if phase == "1":
		file.close()
		return content
	elif phase == "2":
		data = h.findall(content)
		i = 1
		for pvp in data:
			location = content.find(pvp)
			length = len(pvp)
			location_end = location+length
			replacement = content[location:location_end]
			new = content.replace(replacement,str(i)+replacement+str(i))
			i += 1
			content = new
		file.close()
		return content
	elif phase == '3':
		data = h.findall(content)
		return data

def WriteToFile(filewithpath,resultdict):
	file = open(filewithpath,'r+')
	content = file.read()
	content = content.replace('<i>','<I>').replace('</i>','</I>')
	file.close()
	if content == '':
			raise CustomError ("Empty file selected for replacement")
	for each in resultdict:
		l = resultdict[each]
		link = l[0]
		pvp = each
		#print(each,resultdict[each])
		location = content.find(pvp)
		length = len(pvp)
		location_end = location+length
		replacement = content[location:location_end]
		new = content.replace(replacement,replacement+" "+link)
		content = new
	#print(content)
	file = open(filewithpath,'w')
	file.write(content)
	file.close()
	
	
def check_replacements(filewithpath,pvps,resultdict):
	#print(pvps,resultdict)
	for a in pvps:
		if a not in resultdict:
			failure = True
	if len(pvps)!=len(resultdict):
		#print('Hey')
		failure = True
		#print(failure)
	if failure == True:
		return failure
	else:
		return False
			
			
#'''		
phase = "3"
product = "HED"
USER ="Admin"
fileidstr = "15954"
filewithpath="/root/project/pvp_citation/sample/15954.xml"
'''
phase = str(sys.argv[1])
product = str(sys.argv[2])
USER =str(sys.argv[3])
fileidstr = str(sys.argv[4])
filewithpath=str(sys.argv[5])
#'''
t_start = time.time()
t = datetime.date(datetime.now())
fileid = int(fileidstr)

resultd,result,date,UNQLIST,LIST,unq,resultdict,pvps = {},[],[],[],[],[],{},{}
a = re.compile('<I>([^<]+\s+v.\s+[^<]+)</I>', re.IGNORECASE)
b = re.compile('<I>([^<]+ v.[^<]+)</I>\s+\n(<XREF [^>]+>[^<]+</XREF>)', re.MULTILINE)
c = re.compile('<I>([^<]+)</I>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)
e = re.compile('<ITALIC>([^<]+\s+v.\s+[^<]+)</ITALIC>', re.IGNORECASE)
f = re.compile('(<ITALIC>[^<]+ v.[^<]+</ITALIC>)\s+\n(<XREF [^>]+>[^<]+</XREF>)', re.MULTILINE)
g = re.compile('<ITALIC>([^<]+)</ITALIC>', re.IGNORECASE)
h = re.compile('(<I>[^<]+\s+v.\s+[^<]+</I>)', re.IGNORECASE)
i = re.compile('(<I>[^<]+ v.[^<]+</I>)\s+<XREF([^>]+)>[^<]*</XREF>',re.MULTILINE)

if phase == "1":
	filewithpath= "plr01.txt"

	
	
content = readdata(filewithpath,phase)
	
#cnx = sql.connect(user='citation', password='opmstech$123', host='172.1.254.182', port="5432" database='citation')
cnx = psycopg2.connect("dbname='citation' user='citation' host='172.1.254.182' password='opmstech$123'")

'''cursor = cnx.cursor()
cursor.execute("insert into public.Users")
for a in cursor:
	print(a)
cursor.close'''

if phase=="1":
	data = b.findall(content)
	'''for each in result1:
	    if int(each[2])>=1995:
	        date.append(each)'''

	for every in data:
	#    new = every[:2]
	    a = every[0].replace("\n"," ")
	    b = every[1].replace("\n","").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
	    q = c.findall(a)
	    unq = ''.join(d.findall(q[0]))
	    result.append((unq,(a,b)))			
       	
#result.append((a,b))		  
#a = re.compile('\s\s+'," ")
#b = re.compile('\s\s+'," ")
  
	
	resultd = dict(result)
	#print(resultd, " \nin ", time.time() - t_start,"s")
	
	
	
	cursor = cnx.cursor()
	
	add = ("INSERT INTO cite ('USER', 'DATE', 'PRODUCT' ,'PVP', 'LINK', 'UNQ', 'STATUS') VALUES (%s, %s, %s, %s, %s, %s, %s)")
	
	for key in resultd:
		value = resultd[key]
		pvp = value[0]
		link = value[1].replace('"','\"')
		#.append((key,val1,val2,unq))
		data = ('MASTER',t,'PLR',pvp,link,key,'DONE')
		#data = ('Alice', t, 'PLR', 'a v. b', '<VGVGVGBVBV>','avb', 'YTP')
		# Insert new record
		cursor.execute(add, data)
		cnx.commit()
	cursor.close
		
	#print(resultd)
	print(time.time()-t_start)	
	
	cnx.close()

if phase =="2":
	failure = False
	try:
		cursor = cnx.cursor()
		
		finsert = ("INSERT INTO "+'"'+"FILES"+'" ("'+"XML_NAME"+'","'+"STATUS"+'"'+") VALUES  ("+str(fileid)+",'YTP')")
		cursor.execute(finsert)
		
		fselect = ("SELECT "+'"'+"XML_NAME"+'","'+"STATUS"+'" from "' +"FILES"+'" Where "'+"XML_NAME"+'"='+str(fileid))
		cursor.execute(fselect)
		'''for a in cursor.fetchone():
			print(a)'''		
		if cursor.fetchone() == '':
				print("Update failed")
				failure == True
		
			
		cursor.close()
		data = h.findall(content)
		for item in data:
			party = item.replace("\n"," ").replace('See ','').replace('e.g., ','').replace('Pages- ','').replace('cf. ','').replace('e.g. ','').replace('f. ','').replace('cf. ','').replace('citing ','').replace('.&rdquo ','').replace('Id.; ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','').replace('<I> ','<I>')
			pvp = item.replace("<I>",'').replace("</I>",'')
			key = ''.join(d.findall(pvp))
			unq= key.replace("\n"," ").replace('See','').replace('e.g.,','').replace('Pages-','').replace('cf.','').replace('e.g.','').replace('f.','').replace('cf.','').replace('citing','').replace('.&rdquo','').replace('Id.;','').replace('see','').replace('also ,','').replace('E.g.,','').replace('Cf.','').replace('<I>','<I>').replace('See,','').replace('see,','').replace('also','').replace('accord','').replace('compare','').replace('<I>','<I>')
			LIST.append((party,unq))
			#print(LIST)
		
			cursor = cnx.cursor()
			#select = ("SELECT 'ID','STATUS' FROM cite WHERE 'UNQ'= '"+q+"'")
			add = ("INSERT INTO cite ("+'"'+"USER"+'"'+", "+'"'+"DATE"+'"'+", "+'"'+"PRODUCT"+'"'+", "+'"'+"PVP"+'"'+", "+'"'+"UNQ"+'"'+", "+'"'+"STATUS"+'"'+") 	VALUES  (%s, %s, %s, %s, %s, %s)")
			#select = ("SELECT "+'"'+"ID"+'"', +'"'+"PRODUCT"+'"'+,+'"'+"STATUS"+'"'+ "FROM cite Where"+'"'+"UNQ"+'" = '+"'"+unq[1]+"' AND "+'"'+"PRODUCT"+'" =  '+"'"+product+"'")
			#print(fileid)
			for unq in LIST:
				#print(unq[1])
				#select = ("SELECT 'ID', 'PRODUCT', 'STATUS' FROM cite WHERE 'UNQ'= '"+unq[1]+"' AND 'PRODUCT'= '"+product+"'")
				select = ("SELECT "+'"'+"ID"+'", '+'"'+"PRODUCT"+'", '+'"'+"STATUS"+'"'+" FROM "+'"'+"cite"+'"'+" WHERE "+'"'+"UNQ"+'"= '+"'"+unq[1]+"' AND "+'"'+"PRODUCT"+'"'+"= '"+product+"'")
				#SELECT "ID", "PRODUCT", "STATUS" FROM "cite" WHERE "UNQ"= 'SlatteryvSwissReinsuranceAmCorp'
				cursor.execute(select)
				row = cursor.fetchone()
				'''for row in cursor:
				print(row)'''
				if row is None:
					fetch = ("INSERT INTO "+'"'+"XML_VS_PVP"+'"'+ "( "+'"'+"CITEID"+'"'+","+'"'+"STATUS"+'"'+","+'"'+"PRODUCT"+'"'+") SELECT C."+'"'+"ID"+'"'+",C."+'"'+"STATUS"+'"'+",C."+'"'+"PRODUCT"+'"'+" FROM cite AS C WHERE "+'"'+"UNQ"+'"'+" = '"+unq[1]+"'")
			#update = ("UPDATE 'XML_VS_PVP' SET 'XMLID'='ID' , 'FILEID'= %s WHERE 1")
					update = ("UPDATE "+'"'+"XML_VS_PVP"+'"'+" SET "+'"'+"FILEID"+'"'+"= %s WHERE 1")
					data_add = (USER,t,product,unq[0],unq[1],'YTP')
					data_query = (fileid)
					cursor.execute(add,data_add)
					cursor.execute(fetch,data_query)
				cnx.commit()
			cursor.close
			
		if failure == False:
			print("Success")
		
	except IOError:
	    print('An error occured trying to read the file.')
	    
	except ValueError:
	    print('Invalid data found in the file.')
	
	except ImportError:
	    print ("NO module found")
	
	except KeyboardInterrupt:
	    print('You cancelled the operation.')
	
	except ConnectionError:
	    print('Connection Error')
	
	except:
	    print("Unexpected error:", sys.exc_info()[0])
	
			
			

if phase == '3':
	try:
		failure = False
		cursor = cnx.cursor()
		# populate unique list
		#print(content)
		for item in content:
			pvp = item.replace("\n"," ").replace('See ','').replace('e.g., ','').replace('Pages- ','').replace('cf. ','').replace('e.g. ','').replace('f. ','').replace('cf. ','').replace('citing ','').replace('.&rdquo ','').replace('Id.; ','').replace('see ','').replace('also , ','').replace('E.g., ','').replace('Cf. ','').replace('<I> ','<I>').replace('See, ','').replace('see, ','').replace('also ','').replace('accord ','').replace('compare ','').replace('<I> ','<I>')
			data = pvp.replace("<I>","").replace("</I>","")
			unq = ''.join(d.findall(data))
			select = ("SELECT "+'"'+"LINK"+'"'+" FROM cite WHERE "+'"'+"UNQ"+'"'+"= '"+unq+"'")
			#print(unq)
			cursor.execute(select)
			for a in cursor:
				pvps[pvp]=a
				if a != (None,):
					resultdict[pvp] = a
				pvps[pvp]=a

			cnx.commit()
		
		cursor.close	
		#print(resultdict)
		'''for res in resultdict:
			if resultdict[res] == (None,):
				del resultdict[res]
		for any in resultdict:
			print('hi')'''
		WriteToFile(filewithpath,resultdict)
		failure = check_replacements(filewithpath,pvps,resultdict)
		#print(failure)
		
		'''if failure:
			raise CustomError("Citation incomplete")'''
		
	except IOError:
	    print('An error occured trying to read the XML file.')
	    
	except ValueError:
	    print('Invalid data found in the XML file.')
	
	except ImportError:
	    print ("NO module found")
	
	except KeyboardInterrupt:
	    print('You cancelled the operation.')
	
	except ConnectionError:
	    print('Connection Error')
	'''if failure !=True:
		print('Success')'''

			