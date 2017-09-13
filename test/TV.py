#from bs4 import BeautifulSoup
import json
import re, urllib3
'''
http = urllib3.PoolManager()

link = "http://api-v3.switchmedia.asia/213/eduTvAsset/getAssets?page=1&itemsPerPage=20"
xml_doc = http.request('GET', link)

'''
file = open("demo.xml","r")
xml_doc = file.read()
file.close()

#soup = BeautifulSoup(xml_doc, "xml")
dictio = {'000':'000000gm', '001':'','003':'AU_MeRP', '005':'', '008':'', '040':'$aAU-MeRP$beng$cAU-MeRP', '245':'', '260':'','300':'', '347':'', '490':'', '500':'', '518':'', '520':'', '521':'', '650':'', '651':'', '700':'', '856':''}
#a = soup.find_all('record')
#print(a,type(a))
'''
alpha = re.compile ('<[^>]+classwith open("EduReport.txt", "rb") as fin:
    content = json.load(fin)
''''''ificationCode="([^"]*)"',re.MULTILINE)
alpha = re.compile ('<record title="([^"]*)" channel="([^"]*)" source="([^"]*)" dateOfBroadcast="([^"]*)" productionYear="([^"]*)" programTitle="([^"]*)" seriesNo="([^"]*)" episodeNo="([^"]*)" duration="([^"]*)" fileSize="([^"]*)" contentType="([^"]*)" mediaType="([^"]*)" regionofBroadcast="([^"]*)" classificationCode="([^"]*)" curriculumCode="([^"]*)" description="([^"]*)" availability="([^"]*)" subtitles="([^"]*)" mediaFileIndicator="([^"]*)" URL="([^"]*)" videoID="([^"]*)" dateLastModified="([^"]*)" dbCode="([^"]*)">')
for each in a:
    result = alpha.findall(str(each))
print(result)
'''

a = re.compile('<record title="([^"]*)" channel="([^"]*)" source="([^"]*)" dateOfBroadcast="([^"]*)" productionYear="([^"]*)" programTitle="([^"]*)" seriesNo="([^"]*)" episodeNo="([^"]*)" duration="([^"]*)" fileSize="([^"]*)" contentType="([^"]*)" mediaType="([^"]*)" regionofBroadcast="([^"]*)" classificationCode="([^"]*)" curriculumCode="([^"]*)" description="([^"]*)" availability="([^"]*)" subtitles="([^"]*)" mediaFileIndicator="([^"]*)" URL="([^"]*)" videoID="([^"]*)" dateLastModified="([^"]*)" dbCode="([^"]*)"><[^0-9]+><electronicFormatType [^0-9]+="([^"]*)">' , re.IGNORECASE)
YYYYMMDD000000 = re.compile('([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])\s+([0-9][0-9]):([0-9][0-9]):([0-9][0-9])')
YYMMDD = re.compile('[0-9][0-9]([0-9][0-9])-([0-9][0-9])-([0-9][0-9])')
YYYYMMDD = re.compile('([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])')
TTTTTT = re.compile('([0-9][0-9]):([0-9][0-9]):([0-9][0-9])',re.IGNORECASE)
YYYY = re.compile('([0-9][0-9][0-9][0-9])')
contrib = re.compile('<contrib _value="([^"]+)">')
contribRole = re.compile('<contribRole _value="([^"]+)">')
result = a.findall(xml_doc)

for x in result:
	dictio['001'] = x[20]
	Date = YYYYMMDD000000.findall(x[21])
	dictio['005'] = float(''.join(Date[0])+'.0')
	date = YYMMDD.findall(x[21])
	year = YYYY.findall(x[21])
	dictio['008'] = ''.join(date[0])+'s'+''.join(year[0])+'    at                  eng'
	#'at' currently at position 15-16
	dictio['245'] = '00$a'+x[0]
	if x[4] == '':
		YEAR = YYYY.findall(x[3])
		year260 = YEAR[0]
	else:
		year260 = x[4]
	dictio['260'] = '  $aPlace of publication not identified :$b'+x[1]+', $c '+year260
	# assumption that no contributor role will be mentioned anywhere in the document
	dictio['300'] = '  $a1 streaming video file '+x[8]+':$c'+x[9]
	dictio['347'] = '  $a video file ; $b '+x[23]
	if x[6]=='' and x[7]=='':
		data490 = '$a '+x[5]
	else:
		data490 = '$a '+x[5]+' ; $v Series '+x[6]+', Episode '+x[7]
	dictio['490'] = '0 '+data490
	if x[17] =='Yes':
		dictio['500'] = '  $aClosed captioning in English'
	date518 = YYYYMMDD.findall(x[3])
	time518 = TTTTTT.findall(x[3])
	dictio['518'] = '  $aBroadcast '+''.join(date518[0])+' at '+''.join(time518[0])
	if x[15] != '':
		dictio['520'] = '  $a'+x[15]
	dictio['521'] = '8 $aClassification: '+x[13]
	#classification code added
	dictio['650'] = ' 7$aTelevision broadcasting$xFinance.$2fast'
	#default added cli clarification required
	dictio['651'] = ' 7$aVictoria$xMelbourne.$2fast'
	contrib700=contrib.findall(src)
	contribR700=contribRole.findall(src)
	for i in range (1,len(contrib700)):
		c700=contrib700[i]
		cR700=contribR700[i]
		cval='$a'+c700+', $e'+cR700
	
	#dictio['700'] = '1 $a '+contrib700[0]+', $e [ContributorRole]'+contribR700[0]+'$a'+c700+str(i)+', $e'+cR700+str(i)

	#cli input needed
	dictio['856'] = '40'+x[19]
	print(dictio['260'])
	with open("EduReport.txt", "a") as myfile:
		for key in dictio:
			if dictio[key] != '':
				myfile.write('='+key+'  '+str(dictio[key])+ '\n')
		myfile.write('\n')
		myfile.close()

	with open("EduReport.json", "a") as fout:
	    json.dump(dictio, fout, indent=1)
#print(content)
'''with open("EduReport.txt", "rb") as fin:
    content = json.load(fin)
'''