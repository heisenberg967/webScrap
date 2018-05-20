##Python Web Scrapper by Rishab Ravi

##imports
import requests
from BeautifulSoup import BeautifulSoup
import pandas as pd
import csv

##to be appended to
records = []
records2 = []
records3 = []
records4 = []
records5 = []
url="https://www.findinall.com/travel-category-1200"

##form data 
data = { 
'featured':'', 
'keyword': '',
'ads_cat_id': '1200',
'ads_sub_cat_id': '',
'city': '',
'per_page': '500',
'sort_by': ''
}

response = requests.post(url, data=data)
html = response.content
soup = BeautifulSoup(html)


##Start
soup_1 = soup.findAll('div',attrs={'class': 'mt15'})
for res in soup_1:
	
	main = res.findAll('div',attrs={'class':'fl w70 p10'})
	
	for result in range(0,len(main)):
		
		##Company name
		a = main[result].findAll('p',attrs={'class':'wine fs14 b'})
		for i in range(0,len(a)):
			nam = a[i].text[:]
			records.append(nam)

		##Established/size
		b = main[result].findAll('p',attrs={'class':'orange tahoma fs11 lht-16'})
		for j in range(0,len(b)):
			est = b[j].text[16:20]
			estn = filter(str.isdigit,str(est))
			records2.append(estn) ##year establised
			siz = b[j].text[20:]
			sizn = filter(str.isdigit,str(siz))
			records3.append(sizn) ##no of employees
    	##Location
		c = main[result].findAll('p',attrs={'class':'mt7'})
		for k in range(0,len(c)):
			loc = c[k].text[10:]
			records4.append(loc)

	left = res.findAll('div',attrs={'class':'list-left ar fr'})
	
	for result2 in range(0,len(left)):
		##Contact Info
		d = left[result2].findAll('p',attrs={'class':'fs13 black mt5'})
		for l in range(0,len(d)):
			con = d[l].text[:]
			records5.append(con)




df = pd.DataFrame(records,columns=['Company Name'])
df2 = pd.DataFrame(records2,columns=['Year Established'])
df3 = pd.DataFrame(records3,columns=['No. of employees'])
df4 = pd.DataFrame(records4,columns=['Address'])
df5 = pd.DataFrame(records5,columns=['Contact Info'])


frames=[df,df2,df3,df4,df5]
result=pd.concat(frames, axis=1)
result.to_csv("travelCompaniesList.csv",index=False,encoding='utf-8')

