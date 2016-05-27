#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from keys import *

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:

#Your Keys are in another castle

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

auth.secure=True
authUrl = auth.get_authorization_url()

#go to this url
print("Please Visit This link and authorize the app ==> " + authUrl)
print("Enter The Authorization PIN")

#print(ACCESS_KEY)
#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#writing access tokes to file
pin = input().strip()
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens","w")
accessTokenFile.write(token[0]+'\n')
accessTokenFile.write(token[1]+'\n')


#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#        print(tweet.text)

#for line in f:
#        api.update_status(line)
#        time.sleep(900)#Tweet every 15 minutes
