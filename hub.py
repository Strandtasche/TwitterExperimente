#!/usr/bin/env python

import tweepy, time, sys
import datetime, requests, json

option = str(sys.argv[1])

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
