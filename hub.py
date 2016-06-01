#!/usr/bin/env python

import tweepy, time, sys
import datetime, requests, json
from keys import *

option = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if option == "match":
    player = None
    count = None
    #print(len(sys.argv))
    if len(sys.argv) > 2:
        player = str(sys.argv[2])
    if len(sys.argv) > 3:
        count = int(sys.argv[3])
    from getrecentmatch import * 
    print(getRecentMatch(player, count))
    #tweet something?

elif option == "fad":
    query = None
    if len(sys.argv) > 2:
        query = str(sys.argv[2])
    max_tweets = 2
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print("error")
            break
    for x in searched_tweets:
       print(x.text)
