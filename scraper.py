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

states_re = re.compile(r'''<caption\sid="state-(\w+)''', re.X)
district_re = re.compile(r'''\((\d{3})\)\s(\d{3})-(\d{4})''', re.X)

states = states_re.finditer(page)
dis = district_re.finditer(page)

#seed a loop make sure all entries go through

first = np.array([])
second = np.array([])

for item in states:
    first = np.append(first,item.group(0))

for item in dis:
    second= np.append(second,item.group(1))
    
df = pd.DataFrame(first, second)

print(first, second)
