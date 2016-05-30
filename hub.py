#!/usr/bin/env python

import tweepy, time, sys
import datetime, requests, json

option = str(sys.argv[1])

if option == "match":
    from getrecentmatch import * 
    print(getRecentMatch())
