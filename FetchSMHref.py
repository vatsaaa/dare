#Read CSV, column HREFLink
#Navigate to each link and fetch data from their respective page
#Save the data to CSV file
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
webdriver_service = Service("./chromedriver") #Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

hrefmydata = pd.read_csv("D:\RarityData\RarityAllCollections_data.csv")
test=hrefmydata.loc[:,"HREFLink"]#pick data from column
twitter=[]
instagram=[]
discord=[]
cryptowebsite=[]
for eachitem in  (test):
    #print(eachitem)
    driver.get(eachitem)
    driver.maximize_window()

    time.sleep(20)
    #Website Block
    try:
        websitehref = driver.find_element(By.LINK_TEXT,'Website').get_attribute("href")
        print(websitehref)
        cryptowebsite.append(websitehref)
    except NoSuchElementException:
        cryptowebsite.append("No Data")

    #Twitter Block
    try:
        twitterhref=driver.find_element(By.LINK_TEXT,'Twitter').get_attribute("href")
        twitter.append(twitterhref)
    except NoSuchElementException:
        twitter.append("No Data")
    #Discord Block
    try:
        discordhref=driver.find_element(By.LINK_TEXT,'Discord').get_attribute("href")
        discord.append(discordhref)
    except NoSuchElementException:
        discord.append("No Data")
    #Instagram Block
    try:
        instagramhref=driver.find_element(By.LINK_TEXT,'Instagram').get_attribute("href")
        instagram.append(instagramhref)
    except NoSuchElementException:
        instagram.append("No Data")


hrefmydata["TwitterLink"] = twitter
hrefmydata["InstagramLink"] = instagram
hrefmydata["DiscordLink"] = discord
hrefmydata["CryptoWebsite"] = cryptowebsite

# Export to csv
hrefmydata.to_csv("D:\RarityData\RaritywithLinks_data.csv", index=False)