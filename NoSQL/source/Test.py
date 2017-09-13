import csv, sys, re
#import pprint as pp
import psycopg2
import json
import codecs

def csv_reader(file_obj):
	reader = csv.DictReader(file_obj)
	for a in reader:
		print(json.dumps(a))
	return reader


'''def get_attribute(filename):
	file = (filename,'r')
	content = file.read()
	file.close()	
	return content'''

cnx = psycopg2.connect("dbname='TestFiles' user='Test' host='172.1.254.182' password='Pass1234'")
shelf =  re.compile("[^.]+_([\d]+)_[^'csv']+.csv")
ifilename = re.compile("[a-zA-Z0-9_/]+/([\S+]+_input).csv")
kfilename = re.compile("[a-zA-Z0-9_/]+/([\S+]+_keywords).csv")
afilename = re.compile("[a-zA-Z0-9_/]+/([\S+]+_attributes).txt")
dict_list = []


if __name__ == "__main__":
   data_path = "/root/project/NoSQL/sample/software_443023_aug.25.2017_entertainment_reattribution_input.csv"
   #data_path = sys.argv[1]
   kw_path = "/root/project/NoSQL/sample/software_443023_aug.25.2017_entertainment_reattribution_keywords.csv"
   #kw_path = sys.argv[2]
   attr_path = "/root/project/NoSQL/sample/software_443023_aug.25.2017_entertainment_reattribution_attribute.txt"
   #attr_path = sys.argv[3]
   
   try:
	   DataFile = ifilename.findall(data_path)
   except:
	   print("Incorrect input file format")
	   
   try:
	   KeywordFile = kfilename.findall(kw_path)
   except:
	   print("Incorrect keyword file format")	
	   
   try:
	   AttrFile = afilename.findall(attr_path)
   except:
	   print("Incorrect attribute file format")
	   
	   
   Shelf = shelf.findall(data_path)
   DataFileName = DataFile[0]
   KeywordFileName = KeywordFile[0]
   #Attr = get_attribute(attr_path)
   
   with codecs.open(data_path, "r",encoding='utf-8', errors='ignore') as f_obj:
	   data = csv_reader(f_obj)
   
   
	   '''for line in data:
		   dict_list.append(line)
   cursor = cnx.cursor()
   insert = ("INSERT INTO cards ("+'"'+'id'+'","'+'board_id'+'","'+'data'+'"'+") VALUES (%s, %s, %s)")
   
   #data = list(dict_list)
   i = 1
   for a in dict_list:
	   shelf_id = a['primary_shelf (id)'].split(",")
	   if len(shelf_id)>1:
		   ID = a['product_id']+a['item_id']+shelf_id[0]+shelf_id[1]
	   else:
		   ID = a['product_id']+a['item_id']+shelf_id[0]
	   data = (i,ID,json.dumps(a))
	   #cursor.execute(insert, data)
	   i += 1
	   #print(ID)'''
	   
	   
	
		
'''kw_path = "beauty_12345_aug.31.2017_entertainment_reattribution_keywords.csv"
    with open(kw_path, "r") as f_obj:
        csv_reader(f_obj)	'''
	
	 
	 