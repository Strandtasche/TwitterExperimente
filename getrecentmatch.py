import time, sys
import datetime, requests, json
from keys import *

def getRecentMatch(id=None, count=None):
    if id == None:
        id = str(51148205)

    if count == None:
        count = 1

    matchrequest = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?account_id=' + id + '&key=' + STEAM_API_KEY + '&matches_requested=1' 
    r = requests.get(matchrequest)


    if r.status_code != 200:
        print("responsecode != 200, but rather " + str(r.status_code))
        #maybe error handling?
        exit()
    else:
        data = r.json()
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        current = open('currentGame', 'r')
        print(current)


