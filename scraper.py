import urllib.request
import re
import numpy as np
import pandas as pd

#Requests url's html, set write permission to save file then to read
url = "https://www.house.gov/representatives"
with urllib.request.urlopen(url) as request:
    contents = request.read().decode()
with open("wiki_page", "w", encoding = "utf8") as page:
    page.write(contents)  
with open("wiki_page", "r", encoding = "utf8") as page:
    page = page.read()

#Creates a string to search text postions for asstalished info
                        #states_re = re.compile(r'''<caption\sid="state-(\w+)''', re.X)
name_re = re.compile(r'''Bvid=\d\d\d">(.+,\s?.+)</a>|.house.gov/index.cfm
/home">(.+,\s?.+)</a>|.house.gov\/?">(.+,\s?.+)</a>''', re.X)
district_re = re.compile(r'''\((\d{3})\)\s(\d{3})-(\d{4})''', re.X)

#Gets info from the re positions
                        #states = states_re.finditer(page)
dis = district_re.finditer(page)
name = name_re.finditer(page)

#Create array to seed loops
first = []
second = []

#AAdd scrapped data to arrays in desired
for i in name:
    first = np.append(first,i.group(1))
for j in dis:
    second= np.append(second,j.group(0))

#Change array to lists 
nameList = first.tolist()
districtList = second.tolist()

#PLEASE COMMENT THIS CODE :)
if(len(first)>len(second)):
    districtList.extend(['X'] * (len(nameList)-len(districtList)))
else:
    nameList.extend(['X'] * (len(districtList)-len(nameList)))  
temp = {'Name': nameList, 'PhoneNumber': districtList}
df = pd.DataFrame(temp)
print(df)
print(df.Name.to_string(index=False))