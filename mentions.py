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
        output = ""
        #datafile = open("data.json", "w")
        #datafile.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        #datafile.close()
        if (data['result']['radiant_win']):
            output += "Radiant"
            score_winner = data['result']['radiant_score'] - 1
            score_loser = data['result']['dire_score'] - 1
        else:
            output += "Dire"
            score_loser = data['result']['radiant_score'] - 1
            score_winner = data['result']['dire_score'] - 1
        #print(len(data['result']['players']))
        output += " won with " + str(score_winner) + " to " +str(score_loser) + ". Details: https://yasp.co/matches/" + str(matchId) 
        return output

