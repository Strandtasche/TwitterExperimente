#!/usr/bin/env python

import tweepy, time, sys

argfile = str(sys.argv[1])

from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


api.update_status("das 140 zeichen Limit ist doof!")
