import re, time

t_start = time.time()

file = open('c.txt','r')
content = file.read()
file.close()

resultd,result,date = {},[],[]
#b = re.compile('(<I>[^<]* v.[^<]*</I>)[^\s]*\s+[^\s]*\s+(\[\s+[^\]]+\])[^\(]*\([^)]+\s+([1-2][0-9][0-9][0-9])\)', re.MULTILINE)
b = re.compile('(<parties>[^<]* v.[^<]*</parties>)\n<ct-citation-line flow-type="paragraph">\([^\)]*([1-2][0-9][0-9][0-9])\)[^<]+<fill>(<[^>]+>[^<]+</xref>)</ct-citation-line>', re.MULTILINE)

result1 = b.findall(content)
for each in result1:
    if int(each[1])>=1995:
        date.append(each)
for every in date:
    new = every[:1]+every[2:]
    a = new[0].replace("parties","I")
    b = new[1].replace("\n","").replace("[<","[ <").replace(' LINK-STATUS="ACTIVE"',"").replace(' EFFECT="DEFAULT"',"").replace(' RELATE="NO"',"")
    result.append((a,b))
print(result, " \nin ", time.time() - t_start,"s")

resultd = dict(result)
print(resultd, " \nin ", time.time() - t_start,"s")

with open("opc.txt", "w") as myfile:
    for key in resultd:
            myfile.write(key + "\t"+ (resultd[key]) + "\n")
    myfile.close()
    
with open("test.txt", "w") as myfile:
    for key in resultd:
            myfile.write(resultd[key] + "\n")
    myfile.close()
#print(resultd['<I>Southard v. Texas Board of Criminal Justice</I>'], " \nin ", time.time() - t_start,"s")
