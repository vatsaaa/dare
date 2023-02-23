#Read CSV, column TwitterLink
#Navigate to each link and fetch data from their respective page
#Save the data to CSV file
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException

#Chrome Settings
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
webdriver_service = Service("./chromedriver") #Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#Read csv file
hrefmydata = pd.read_csv("D:\RarityData\RaritywithLinks_data.csv")
twitterlink=hrefmydata.loc[:,"TwitterLink"]#pick data from column
#list to collect data
twitterhandle=[]
NoOfTweets=[]
NoOfFollw=[]
CreatedOndate=[]

for eachitem in twitterlink:
    if eachitem=='No Data':
        twitterhandle.append("No Data")
        NoOfFollw.append("No Data")
        NoOfTweets.append("No Data")
        CreatedOndate.append("No Data")
    else:

        driver.get(eachitem)
        driver.maximize_window()
        time.sleep(15)
    #Handle block
        try:
            handledata=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span').text
            twitterhandle.append(handledata)
        except NoSuchElementException:
            twitterhandle.append("No Data")
    #Number of tweets
        try:
            NoOfTweetsdata=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div').text
            NoOfTweetsdata.replace("Tweet","").strip()
            NoOfTweets.append(NoOfTweetsdata)
        except NoSuchElementException:
            NoOfTweets.append("No Data")
    #Number of Followers
        try:
            NoOfFollwdata=driver.find_element(By.XPATH,'//span[contains(text(), "Followers")]/ancestor::a/span').text
            print(type(NoOfFollwdata))
            if "M" in NoOfFollwdata:
                NoOfFollwdata.replace("M","")
                NoOfFollwdata=str(int(float(NoOfFollwdata)*1000000))
            if "K" in NoOfFollwdata:
                NoOfFollwdata.replace("K","")
                print(NoOfFollwdata)
                NoOfFollwdata=str(int(float(NoOfFollwdata)*1000))
            NoOfFollw.append(NoOfFollwdata)
        except NoSuchElementException:
            NoOfFollw.append("No Data")
    #Created on data
        try:
            CreatedOndatedata=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span[2]/span').text
            CreatedOndatedata=CreatedOndatedata.replace("Joined","")
            CreatedOndate.append(CreatedOndatedata)

        except NoSuchElementException:
            CreatedOndatedata = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[4]/div/span/span').text
            CreatedOndatedata = CreatedOndatedata.replace("Joined", "")
            CreatedOndate.append(CreatedOndatedata)

hrefmydata["TwitterHandle"]=twitterhandle
hrefmydata["NoOfTweets"]=NoOfTweets
hrefmydata["NoOfFollower"]=NoOfFollw
hrefmydata["TCreatedOndate"]=CreatedOndate

hrefmydata.to_csv("D:\RarityData\RaritywithLinks_data.csv", index=False)