import nltk
from collections import Counter

def loadDictionary():
    dictionaryFile = open('dict.txt')
    englishWords = []
    for word in dictionaryFile.read().split('\n'):
        englishWords.append(word)
    dictionaryFile.close()
    return englishWords

titles = loadDictionary()

file = open('ARB6867.xml','r')
content = file.read()
file.close()

text = nltk.word_tokenize(content)
tagged = nltk.pos_tag(text)
result,shortlist,newresult,actualwords,dummy,rev,final,possible,names = [],[],[],[],[],[],[],[],[]

for every in tagged:
    tag = every[1]
    if tag == 'NNP':
        result.append(every)
        
for entity in result:
    a = entity[0]
    newresult.append(a)
                    
alpha = list(set(newresult))

for a in alpha:
    for ch in list(a):
        if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            flag = True
        else:
            flag = False
            break
    if flag:
        actualwords.append(a)
        
for i in actualwords:
    if ((i == i.title()) and (3 <= len(i))):
        dummy.append(i)        

for x in (set(titles) & set(dummy)):
    dummy.remove(x)
      
for i in range(0,len(dummy)-1):
    for j in range (0,len(dummy)):
        a = dummy[i]+' '+dummy[j]
        if a in str(content):
            rev.append(a)
        b = dummy[j]+' '+dummy[i]
        if b in str(content):
            rev.append(b)
            
shortlist = set(rev)         
final = [x.split() for x in shortlist]
new = [inner for outer in final for inner in outer]
                
count = Counter(new)    
absolute = [k for k, v in count.items() if v == 1]
#

for i in range(0,len(absolute)-1):
    for j in range (0,len(absolute)):
        a = absolute[i]+' '+absolute[j]
        possible.append(a)

for x in (set(possible) & set(rev)):
    names.append(x)
print(count,'\n',final)
print(*names, sep=", ")

with open('result.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(names))
myfile.close()
#print(actualwords,len(actualwords))'''