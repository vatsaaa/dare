# Fetch All Collections data from rarity.tools
# Save the data into a ".csv" file

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
webdriver_service = Service("./chromedriver")  # Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
url = "https://rarity.tools/"
driver.get(url)
driver.maximize_window()
time.sleep(15)
# accept cookie
soup = BeautifulSoup(driver.page_source, 'html5lib')
table1 = soup.find('table', class_="relative m-auto dataTable")

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

mydata = pd.DataFrame(columns=headers)
# Create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# mydata.head()
hreflist = []
for link in table1.find_all('a'):
    hrefdata = "https://rarity.tools" + link.get('href')
    hreflist.append(hrefdata)

mydata["HREFLink"] = hreflist
# Export to csv
mydata.to_csv("D:\RarityData\RarityAllCollections_data.csv", index=False)
