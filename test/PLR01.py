import re, time

t_start = time.time()
file = open('plr01.txt','r')
content = file.read()
file.close()


resultd,result,date = {},[],[]
b = re.compile('(<ITALIC>[^<]+v.[^<]+</ITALIC>)[^\[<]*\[\n<SMALL-CAP>[^<]+</SMALL-CAP>\s+\n(<XREF[^<]+</XREF>)\][^(]+\([^)]+\s+([1-2][0-9][0-9][0-9])\)', re.MULTILINE)
#rep = {"condition1": "", "condition2": "text"}
#b = re.compile('(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[\s+[^\]]+\])', re.MULTILINE)
#(<I>[^<]* v. [^<]*</I>)[^\s]*\s+(\[[^\]]+\])
#((&lsqb;|\[)[^\[]*(&rsqb;|\]))
#a = re.compile('<I>([^<]* v. [^<]*)</I>')
result1 = b.findall(content)
#DB = dict(result1)
for each in result1:
    if int(each[2])>=1995:
        date.append(each)
for every in date:
    new = every[:2]
    a = new[0].replace("\n"," ").replace('<ITALIC>','<I>').replace('</ITALIC>','</I>')
    b = new[1].replace("\n","").replace("[<","[ <").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
    #a = re.compile('\s\s+'," ")
    #b = re.compile('\s\s+'," ")
    result.append((a,b))

resultd = dict(result)
print(resultd, " \nin ", time.time() - t_start,"s")

'''with open("PLR01.txt", "w") as myfile:
    for key in resultd:
            myfile.write(key + "\t"+ (resultd[key]) + "\n")
    myfile.close()
    
with open("test.txt", "w") as myfile:
    for key in resultd:
            myfile.write(resultd[key] + "\n")
    myfile.close()
'''
#print(resultd['<I>Southard v. Texas Board of Criminal Justice</I>'], " \nin ", time.time() - t_start,"s")
