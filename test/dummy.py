from bs4 import BeautifulSoup
import re, json
import requests
i = 1500
status = True
url = "http://api-v3.switchmedia.asia/213/eduTvAsset/getAssets?page="+str(i)+"&itemsPerPage=20"
r  = requests.get(url)
	
data = r.text
soup = BeautifulSoup(data,"lxml")
	
if len(soup.find_all('record'))==0:
	status == False
else:
	status == True
while status == True:
	for i in range(0,20):
		print('hi')
		
	