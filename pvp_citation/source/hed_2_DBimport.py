from bs4 import BeautifulSoup
import re, time
LIST = []
t_start = time.time()
file = open("alpha.html","r")
sgml_doc = file.read()
file.close()

#soup = BeautifulSoup(sgml_doc, "html.parser")
'''
for a in soup.find_all(:
    LIST.append(a)
'''
#print(sgml_doc)
a = re.compile('<i>([^<]*) v. ([^<]*)</i>([^ ]*)(&lsqb;|\\[)([^\\[]*)(&rsqb;|\\])')
result = a.findall(content)


for a in soup.find_all(text = re.compile('<I>([^<]*v.[^<]*)</I>')):
    LIST.append(a) 
    
print(LIST,"in time:",time.time() - t_start)

LIST1 = []
t1_start = time.time()

for a in soup.find_all(text = re.compile('<I>([^<]*v.[^<]*)</I>([^ ]* (&lsqb;|\[)[^\[]*(&rsqb;|\]))')):
    LIST1.append(a) 
    
print(LIST1,"in time:",time.time() - t1_start)
#<i>([^<]*v.[^<]*)</i>([^ ]* (&lsqb;|\[)[^\[]*(&rsqb;|\]))
  
#print("Elements:",soup.find_all('I'),"in time:",time.time() - t_start,"sec")
