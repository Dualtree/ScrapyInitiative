import urllib.request
import re
import numpy as np
import pandas as pd

url = "https://www.house.gov/representatives"

with urllib.request.urlopen(url) as request:
    contents = request.read().decode()

with open("wiki_page", "w", encoding = "utf8") as page:
    page.write(contents)  

with open("wiki_page", "r", encoding = "utf8") as page:
    page = page.read()

#states_re = re.compile(r'''<caption\sid="state-(\w+)''', re.X)
name_re = re.compile(r'''.house.gov\/?">(.+),\s(.+)</a>''', re.X)
district_re = re.compile(r'''\((\d{3})\)\s(\d{3})-(\d{4})''', re.X)

#states = states_re.finditer(page)
dis = district_re.finditer(page)
name = name_re.finditer(page)

first = []
second = []

for i in name:
    first = np.append(first,i.group(0))

for j in dis:
    second= np.append(second,j.group(0))

nameList = first.tolist()
districtList = second.tolist()

if(len(first)>len(second)):
    districtList.extend(['X'] * (len(nameList)-len(districtList)))
else:
    nameList.extend(['X'] * (len(districtList)-len(nameList)))

    
temp = {'Name': nameList, 'PhoneNumber': districtList}

df = pd.DataFrame(temp)
print(df)
print(df.Name.to_string(index=False))