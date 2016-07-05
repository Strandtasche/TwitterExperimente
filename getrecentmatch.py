import time, sys
import datetime, requests, json
from keys import *

def getRecentMatch(id=None, count=None):
    if id == None:
        id = str(51148205)

    if count == None:
        count = 1

    player = 'Strandtasche'

    matchRequestAccId = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?account_id=' + id + '&key=' + STEAM_API_KEY + '&matches_requested=' + str(count)

    #matchRequestUsrnm = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=' + STEAM_API_KEY + '&player_name=' + player + 'matches_requested=' + str(count)

    r = requests.get(matchRequestAccId)

    if r.status_code != 200:
        print("responsecode != 200, but rather " + str(r.status_code))
        exit()
    else:
        data = r.json()
        output = ""
        datafile = open("dataName.json", "w")
        datafile.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        datafile.close()
