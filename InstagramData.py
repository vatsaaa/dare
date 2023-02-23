#Read CSV, column InstagramLink
#Navigate to each link and fetch data from their respective page
#Save the data to CSV file
import pandas as pd
import instaloader

instaProfileLinks=pd.read_csv(r"D:\RarityData\RaritywithLinks_data.csv",header=0,usecols=["InstagramLink"])
print(type(instaProfileLinks))
for eachlink in instaProfileLinks:
    print(eachlink)
    bot = instaloader.Instaloader()
# Loading the profile from an Instagram handle
    print(eachlink.partition("/")[0])
    #profilename=eachlink.s
    profile = instaloader.Profile.from_username(bot.context, 'azuki')
    print(profile)
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    print("Bio: ", profile.biography)
    print("External URL: ", profile.external_url)


"""
#list to collect data
twitterhandle=[]
NoOfTweets=[]
NoOfFollw=[]
CreatedOndate=[]
"""