import sys
import re, json, time
import requests
from bs4 import BeautifulSoup

def urlextraction(i):
   url = "http://api-v3.switchmedia.asia/213/eduTvAsset/getAssets?page="+str(i)+"&itemsPerPage=20"
   r = requests.get(url)
   data = r.text
   soup = BeautifulSoup(data,"lxml")
   print(soup.find_all('record'))
   if len(soup.find_all('record'))==0:
	   print("no more records to display",time.time()-t_start)
	   sys.exit()
   else:
	   dictio = {'000':'000000gm', '001':'','003':'AU_MeRP', '005':'', '008':'', '040':'$aAU-MeRP$beng$cAU-MeRP', '245':'', '260':'','300':'', '347':'', '490':'', '500':'', '518':'', '520':'', '521':'', '650':'', '651':'', '700':'', '856':''}
	   for rec in soup.find_all('record'):
		   z = a.findall(str(rec))
		   print(i)
		   x = z[0]
		   dictio['001'] = x[22]
		   #Date = YYYYMMDD000000.findall(x[21])
		   Date = time.strftime("%Y%m%d%H%M%S")
		   #dictio['005'] = float(''.join(Date[0])+'.0')
		   dictio['005'] = float(Date+'.0')
		   #date = YYMMDD.findall(x[21])
		   date = time.strftime('%y%m%d')
		   year = time.strftime('%Y')  
		   #year = YYYY.findall(x[21])
		   dictio['008'] = date+'s'+year+'    at                  eng'
		   #at' currently at position 15-16
		   dictio['245'] = '00$a'+x[20]+'$c/ Director: '
		   if x[14] == '':
			   YEAR = YYYY.findall(x[6])
			   year260 = YEAR[0]
		   else:
			   year260 = x[14]
		   dictio['260'] = '  $aPlace of publication not identified :$b'+x[1]+', $c '+year260
		   #assumption that no contributor role will be mentioned anywhere in the document
		   dictio['300'] = '  $a1 streaming video file '+x[9]+':$c'+x[11]
		   dictio['347'] = '  $a video file ; $b '+x[22]
		   if x[17]=='' and x[10]=='':
			   data490 = '$a '+x[15]
		   else:
			   data490 = '$a '+x[15]+' ; $v Series '+x[6]+', Episode '+x[7]
		   dictio['490'] = '0 '+data490
		   if x[19] =='Yes':
			   dictio['500'] = '  $aClosed captioning in English'
		   date518 = YYYYMMDD.findall(x[6])
		   time518 = TTTTTT.findall(x[6])
		   dictio['518'] = '  $aBroadcast '+''.join(date518[0])+' at '+''.join(time518[0])
		   if x[8] != '':
			   dictio['520'] = '  $a'+x[8]
		   dictio['521'] = '8 $aClassification: '+x[2]
		   #classification code added
		   dictio['650'] = ' 7$a'+''.join(sub.findall(str(rec)))+'$xFinance.$2fast'
		   #val650 dummy added
		   #default added cli clarification required
		   if len(geo.findall(str(rec)))!=0:
			   geo651=geo.findall(str(rec))  
			   alpha = geo651[0]
			   if alpha[1]=='' and alpha[2]=='':
				   g651 = alpha[3]
				   dictio['651'] = ' 7$a'+g651+'.$2fast'
			   else:
				   a651=alpha[1]
				   x651=alpha[2]   
				   dictio['651'] = ' 7$a'+a651+'$x'+x651+'.$2fast'
		   if len(contrib.findall(str(rec)))!=0:
			   dictio['700'] = '1 $a '+''.join(contrib.findall(str(rec)))+', $e '+''.join(contribRole.findall(str(rec)))
		   #cli input needed
		   dictio['856'] = '40'+x[21]
		   #print(dictio['651'])
	   
		   with open("EduReport.txt", "a") as myfile:
			   for key in dictio:
				   if dictio[key] != '':
					   myfile.write('='+key+'  '+str(dictio[key])+ '\n')
			   myfile.write('\n')
			   myfile.close()
		   with open("EduReport.json", "a") as fout:
			   json.dump(dictio, fout, indent=1)
			   
		   i = i+1
		   urlextraction(i)

		   
a = re.compile('<record availability="([^"]*)" channel="([^"]*)" classificationcode="([^"]*)" contenttype="([^"]*)" curriculumcode="([^"]*)" datelastmodified="([^"]*)" dateofbroadcast="([^"]*)" dbcode="([^"]*)" description="([^"]*)" duration="([^"]*)" episodeno="([^"]*)" filesize="([^"]*)" mediafileindicator="([^"]*)" mediatype="([^"]*)" productionyear="([^"]*)" programtitle="([^"]*)" regionofbroadcast="([^"]*)" seriesno="([^"]*)" source="([^"]*)" subtitles="([^"]*)" title="([^"]*)" url="([^"]*)" videoid="([^"]*)">[^*]+<electronicformattype elecformattype="([^"]*)">',re.IGNORECASE)
#olda = re.compile('<record title="([^"]*)" channel="([^"]*)" source="([^"]*)" dateOfBroadcast="([^"]*)" productionYear="([^"]*)" programTitle="([^"]*)" seriesNo="([^"]*)" episodeNo="([^"]*)" duration="([^"]*)" fileSize="([^"]*)" contentType="([^"]*)" mediaType="([^"]*)" regionofBroadcast="([^"]*)" classificationCode="([^"]*)" curriculumCode="([^"]*)" description="([^"]*)" availability="([^"]*)" subtitles="([^"]*)" mediaFileIndicator="([^"]*)" URL="([^"]*)" videoID="([^"]*)" dateLastModified="([^"]*)" dbCode="([^"]*)"><[^0-9]+><electronicFormatType [^0-9]+="([^"]*)">' , re.IGNORECASE)
YYYYMMDD000000 = re.compile('([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])\s+([0-9][0-9]):([0-9][0-9]):([0-9][0-9])')
YYMMDD = re.compile('[0-9][0-9]([0-9][0-9])-([0-9][0-9])-([0-9][0-9])')
YYYYMMDD = re.compile('([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])')
TTTTTT = re.compile('([0-9][0-9]):([0-9][0-9]):([0-9][0-9])',re.IGNORECASE)
YYYY = re.compile('([0-9][0-9][0-9][0-9])')
contrib = re.compile('<contrib _value="([^"]+)">')
contribRole = re.compile('<contribRole _value="([^"]+)">')
geo = re.compile('<geogLoc _value="(([^"]+)--([^"]+)|([^"]+))">',re.IGNORECASE)
sub = re.compile('<subj _value="([^"]+)">')
t_start = time.time()
urlextraction(1)
