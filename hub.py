#!/usr/bin/env python

import tweepy, time, sys, pytz
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
    if len(sys.argv) == 3:
        query = str(sys.argv[2])
        from fad import foolAndDeploy
        foolAndDeploy(query)
    else:
        print("wrong number of arguments given")

elif option == "highnoon":
    #time =  12 - datetime.datetime.utcnow().hour
    #input_utc_offset = datetime.timedelta(hours=time)
    #timezone_ids = set()
    #now = datetime.datetime.now(pytz.utc)
    #for tz in map(pytz.timezone, pytz.all_timezones_set):
    #    dt = now.astimezone(tz)    
    #    tzinfos = getattr(tz, '_tzinfos', [(dt.tzname(), dt.dst(), dt.utcoffset())])
    #    if any(dst == input_utc_offset for dst, _, _ in tzinfos):
    #        timezone_ids.add(tz.zone)
    #print(timezone_ids)
    home = pytz.timezone('Europe/Berlin')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    highnoon = []
    for i in pytz.common_timezones:
        test = pytz.timezone(i)
        hometime = home.localize(datetime.datetime.now())
        timethere = hometime.astimezone(test)
        #print(timethere.strftime(fmt))
        if timethere.hour == 12:
            highnoon.append(i)
    print(highnoon)

