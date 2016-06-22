import tweepy, time, sys, pytz, random
import datetime, requests, json
from keys import *

def handleRequest(tweetstring):
    inputString = tweetstring.split()
    if len(inputString) < 2 or len(inputString) > 3:
        return "Failed Parse, Invalid Input"

    matchId = int(inputString[1])
    matchrequest = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=" + str(matchId) + "&key=" + STEAM_API_KEY

    r = requests.get(matchrequest)

    if r.status_code != 200:
        print("responsecode != 200, but rather " + str(r.status_code))
        exit()
    else:
        data = r.json()
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

