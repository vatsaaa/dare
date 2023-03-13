#Read CSV, column InstagramLink
#Navigate to each link and fetch data from their respective page
#Save the data to CSV file
import pandas as pd
import instaloader
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys

#Chrome Settings
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)
webdriver_service = Service("./chromedriver") #Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Login to Instagram first for maximum results
# driver.get("https://www.instagram.com/")
#driver.maximize_window()
# time.sleep(10)
# save login credentials on browser
# inputusername=driver.find_element(By.XPATH,r'//*[@id="loginForm"]/div/div[1]/div/label/input')
# inputusername.send_keys("cyborgrpatiger")
# inputpassword=driver.find_element(By.XPATH,r'//*[@id="loginForm"]/div/div[2]/div/label/input')
# inputpassword.send_keys("Test@1234")
# inputusername.send_keys(Keys.ENTER)
#time.sleep(5)
#print("Sleep completed")
#inputNFTData=driver.find_element(By.XPATH, "//input[@placeholder='Search']")

"""driver.get("https://instagram.com/azuki")
inputNFTData=driver.find_element(By.XPATH,r'//*[@id="mount_0_0_*"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div/button').click()
inputNFTData=driver.find_element(By.XPATH,r'//*[@id="mount_0_0_FR"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div/svg').click()
inputNFTData=driver.find_element(By.XPATH, "//input[@placeholder='Search']")
inputNFTData.send_keys("rtfkt")
inputNFTData.send_keys(Keys.ENTER)"""

hrefmydata=pd.read_csv(r"D:\RarityData\RaritywithLinks_data.csv")
instaProfileLinks=hrefmydata.loc[:,"InstagramLink"]
InstaHandle=[]
InstaFollowers=[]
InstaCreatedDate=[]
CreatedBy=[]
AccLoc=[]
InstaPosts=[]
for eachlink in instaProfileLinks:
    if eachlink=="No Data":
        InstaHandle.append("No Data")
        InstaFollowers.append("No Data")
        InstaCreatedDate.append("No Data")
        InstaPosts.append("No Data")
        CreatedBy.append("No Data")
        AccLoc.append("No Data")
    else:

        #Click using Selenium
        #driver.find_element(By.XPATH,'// *[ @ id = "mount_0_0_gF"] / div / div / div / div[1] / div / div / div / div[1] / div[1] / div[2] / section / main / div / header / section / div[1] / div[2] / button / div / svg').click()
        bot = instaloader.Instaloader()
# Loading the profile from an Instagram handle
        print(eachlink.partition(".com/")[2])
        link=eachlink.partition(".com/")[2]
    #profilename=eachlink.s
        profile = instaloader.Profile.from_username(bot.context, link)
        print(profile)
        InstaHandle.append(profile.username)
        InstaPosts.append(profile.mediacount)
        InstaFollowers.append(profile.followers)
        CreatedBy.append("No Data")
        AccLoc.append("No Data")
        InstaCreatedDate.append("No Data")

hrefmydata["InstagramHandle"]=InstaHandle
hrefmydata["InstagramFollowers"]=InstaFollowers
hrefmydata["ICreatedOnDate"]=InstaCreatedDate
hrefmydata["CreatedBy"]=CreatedBy
hrefmydata["IAccountLocation"]=AccLoc
hrefmydata["Ipost"]=InstaPosts

hrefmydata.to_csv("D:\RarityData\RaritywithLinks_data.csv", index=False)

#=//*[@id="mount_0_0_gF"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div


