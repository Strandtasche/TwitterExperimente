#!/usr/bin/env python

import tweepy, time, sys
import datetime, requests, json

#argfile = str(sys.argv[1])

from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


#api.update_status("das 140 zeichen Limit ist doof!")
#tweets =(api.user_timeline("Strandtasche"))
#for t in tweets:
#    print(t.text)

#for i in range(10):
#    otp = str(i) + " "+ str(datetime.datetime.now().second)
#    time.sleep(1)
#    print(otp)

r = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=27110133&key=7D9664892955037443B7E50E163C3019')

if r.status_code != 200:
    print("responsecode != 200")
    #maybe error handling?
    exit()
else:
    data = json.load(r.json())
    #print("success")
