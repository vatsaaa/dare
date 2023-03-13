import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Chrome Settings
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
webdriver_service = Service("./chromedriver") #Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

hrefmydata = pd.read_csv(r"D:\RarityData\RaritywithLinks_data.csv")
discordProfileLinks = hrefmydata.loc[:,"DiscordLink"]

list1=[]
list2=[]
list3=[]

for eachlink in discordProfileLinks:
    if eachlink == "No Data":
        list1.append("No Data")
        list2.append("No Data")
        list3.append("No Data")
    else:
        driver.get(eachlink)
        driver.maximize_window()
        time.sleep(10)
        websitehref = driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/div[2]/div[2]/span').text
        websitehref = websitehref.split(" ")
        list1.append(websitehref[0])
        websitehref1 = driver.find_element(By.XPATH,
                                          '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/div[2]/div[1]/span').text
        websitehref1=websitehref1.split(" ")
        list2.append(websitehref1[0])
        websitehref2 = driver.find_element(By.XPATH,
                                          '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/h1').text

        list3.append(websitehref2)

hrefmydata["DMember"] = list1
hrefmydata["DOnline"] = list2
hrefmydata["DName"] = list3

hrefmydata.to_csv("D:\RarityData\RaritywithLinks_data.csv", index=False)



