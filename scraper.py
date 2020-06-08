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
name_re = re.compile(r'''">(.+,\s?.+)</a>''', re.X)
phoneNumber_re = re.compile(r'''\((\d{3})\)\s(\d{3})-(\d{4})''', re.X)
party_re = re.compile(r'''<td>(D|R|L)\s\s\s\s''', re.X)
district_re = re.compile(r'''<td>(.+?)\s\s\s\s\s\s\s\s<\/td>\n(?:.+?)<td><a href=''', re.X)

#Gets info from the re positions(extracts them)
#states = states_re.finditer(page)
extrName = name_re.finditer(page)
extrPhoneNum = phoneNumber_re.finditer(page)
extrParty = party_re.finditer(page)
extrDistrict = district_re.finditer(page)

#Create array to seed loops
nameArr = []
phoneArr = []
partyArr = []
districtArr = []

#Add scrapped data to arrays in desired
for i in extrName:
    nameArr = np.append(nameArr,i.group(1))
for j in extrPhoneNum:
    phoneArr= np.append(phoneArr,j.group(0))
for k in extrParty:
    partyArr= np.append(partyArr,k.group(1))
for l in extrDistrict:
    districtArr= np.append(districtArr,k.group(1))

#Change array to lists 
nameList = nameArr.tolist()
phoneNumList = phoneArr.tolist()
partyList = partyArr.tolist()
districtList = districtArr.tolist()

#Creates list same size (during testing)
print("Name arr len: " + str(len(nameArr)))
print("Phone num arr len: " + str(len(phoneArr))+"\n\n")
print("Party arr len: " + str(len(partyArr))+"\n\n")
print("District arr len: " + str(len(districtArr))+"\n\n")

#if(len(districtArr)<len(nameArr)):
#   districtList.extend(['X'] * (len(nameList)-len(districtList)))
#else:
#    nameList.extend(['X'] * (len(phoneNumList)-len(nameList)))

#Creates Dataframe (Colomes and Rows)
temp = {'Name': nameList, 'PhoneNumber': phoneNumList, 'Party': partyList, 'District': districtList}
df = pd.DataFrame(temp)
data = df.drop_duplicates()

#Print Section
print(data)

#print(df.loc[df.PhoneNumber=="(202) 225-5265"])
#print(df.Name.to_string(index=False))
#print(df.PhoneNumber.to_string(index=False))
