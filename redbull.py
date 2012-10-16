# This is an extremely dirty, non OOP, done in 6 minutes script to fetch live redbull stratos viewers 
# @author: @javierhonduco

#from bs4 import BeautifulSoup # I firstly thought data wasn't loaded vua js :b
import datetime, time, urllib2, tweepy

ENABLE_TWEETING = False # Pure crap way... Some uneeded stuff is being loaded but... rough prototyping! :)
REQUEST_INTERVAL = 600
OUTPUT = os.basename(__file__) + "/whatever.csv"

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

oldata = 0
api = tweepy.API(auth)

while 1: 
	data = int(urllib2.urlopen("http://www.youtube.com/live_stats?v=MrIxH6DToXQ&t=1350225339022").read()) # A non documented API endopoint... Assuming that no errors will be raised :P
	#soup = BeautifulSoup(data)
	#content = soup.find_all("span", class_= "concurrent-viewers-number")
	time = datetime.datetime.now().strftime("%H:%M:%S %Z")
	if ENABLE_TWEETING:
		api.update_status("viewers: "+ data +" (change of):"+ (data-oldata) +" people, time: " +  time +" #redbullstratos") # string formatting!!
	else:
		open(OUTPUT + ".csv", "a").write(data +", " +  time + "\n")
	print data + ", " + time # Kinda debugging info 
	oldata = int(data)
	time.sleep(REQUEST_INTERVAL)

