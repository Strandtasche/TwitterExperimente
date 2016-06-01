import time, sys
import datetime, requests, json
from keys import *

def getRecentMatch(id=None, count=None):
    if id == None:
        id = "Strandtasche"

    if count == None:
        count = 25

    matchrequest = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?player_name=' + id + '&key=' + STEAM_API_KEY + '&matches_requested=2' 
    r = requests.get(matchrequest)


    if r.status_code != 200:
        print("responsecode != 200, but rather " + str(r.status_code))
        #maybe error handling?
        exit()
    else:
        data = r.json()
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    return "success"


