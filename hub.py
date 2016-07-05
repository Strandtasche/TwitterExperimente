#!/usr/bin/env python

import tweepy, time, sys, pytz, random
import datetime, requests, json
from keys import *

option = str(sys.argv[1])

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    authAlt = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authAlt.set_access_token(ACCESS_KEY_ALT, ACCESS_SECRET_ALT)
    apiAlt = tweepy.API(authAlt)
except:
    print("Couldn't establish connection to Twitter")
    exit()


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
        if timethere.hour == 12 and len(i) > 4 and not (i[0] == 'U' and i[1]=='S') and not i[0] == 'C':
            highnoon.append(i)
    location = random.choice(highnoon)
    location = location.replace("_", " ")
    #print(highnoon)
    temp = location.split('/')
    #print(temp)
    tweetstring = "It's High Noon... In " + temp[1] + " (" + temp[0] + ")"
    #print(len(tweetstring))
    apiAlt.update_status(tweetstring)
    print('Printed successfully')

elif option == "hunting":
    query = None
    if len(sys.argv) == 3:
        query = str(sys.argv[2])
        from fad import huntingforhighnoon
        huntingforhighnoon(query)
    else:
        print("wrong number of arguments given")

elif option == "mentions":
    tasks = api.mentions_timeline(count=5)
    handledLast = open('mentionHandle', 'r')
    lastTweetId = int(handledLast.read())
    from mentions import handleRequest
    print(lastTweetId)
    currentRequests = []
    for i in tasks:
        if (i.id != lastTweetId):
            currentRequests.append(i)
            print("New Tweet: " + i.text)
        else:
            break
    if currentRequests == []:
        print("No new Tweets! exiting...")
        exit()
    for k in currentRequests:
        output = handleRequest(k.text)
        #if output != "Failed Parse, Invalid Input":
            #print(output)
            #print(len(output))
        api.update_status('@' + k.user.screen_name + " " + output, in_reply_to_status_id = k.id) 
        time.sleep(5)

    mostRecentTweet = currentRequests[0].id
    handle = open('mentionHandle', 'w')
    handle.write(str(mostRecentTweet))

