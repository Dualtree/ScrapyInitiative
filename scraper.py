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
name_re = re.compile(r'''Bvid=\d\d\d">(.+,\s?.+)</a>|.house.gov/index.cfm/home">(.+,\s?.+)</a>|.house.gov\/?">(.+,\s?.+)</a>''', re.X)
phoneNumber_re = re.compile(r'''\((\d{3})\)\s(\d{3})-(\d{4})''', re.X)

#Gets info from the re positions(extracts them)
#states = states_re.finditer(page)
extrPhoneNum = phoneNumber_re.finditer(page)
extrName = name_re.finditer(page)

#Create array to seed loops
nameArr = []
phoneArr = []

#Add scrapped data to arrays in desired
for i in extrName:
    nameArr = np.append(nameArr,i.group(1))
for j in extrPhoneNum:
    phoneArr= np.append(phoneArr,j.group(0))

#Change array to lists 
nameList = nameArr.tolist()
phoneNumList = phoneArr.tolist()

#Creates list same size (during testing)
if(len(nameArr)>len(phoneArr)):
    phoneNumList.extend(['X'] * (len(nameList)-len(phoneNumList)))
else:
    nameList.extend(['X'] * (len(phoneNumList)-len(nameList)))

print(nameList)
print("\n")
#Creates Dataframe (Colomes and Rows)
temp = {'Name': nameList, 'PhoneNumber': phoneNumList}
df = pd.DataFrame(temp)

#Print Section
print(df)
print("\n")

#print(df.loc[df.PhoneNumber=="(202) 225-5265"])
#print(df.Name.to_string(index=False))
#print(df.PhoneNumber.to_string(index=False))
