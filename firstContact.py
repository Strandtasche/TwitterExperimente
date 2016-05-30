#!/usr/bin/env python

import tweepy, time, sys
import datetime, requests, json

arg = int(sys.argv[1])
slot= int(sys.argv[2])

if arg < 27110133 or arg > 9395420018 or slot not in range(10):
    print("invalid matchID or slot")
    exit()

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

matchrequest = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=' + str(arg) + '&key=7D9664892955037443B7E50E163C3019'
r = requests.get(matchrequest)

if r.status_code != 200:
    print("responsecode != 200, but rather " + str(r.status_code))
    #maybe error handling?
    exit()
else:
    data = r.json()
    print(json.dumps(data['result']['players'][slot], sort_keys=True, indent=4, separators=(',', ': ')))
    #print("success")
