import tweepy, datetime
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def foolAndDeploy(query):
    max_tweets = 50
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query ,  count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print("error")
            break
    #for x in searched_tweets:
    #   print(x.user.name)
    #   print(x.text)
    return searched_tweets

def huntingforhighnoon(query):
    #searched_tweets = foolAndDeploy(query)
    searched_tweets = api.search(q=query)
    print(len(searched_tweets))
    potentials = []
    #for i in searched_tweets:
        #print(i.text)
        #print(i.created_at)
    potentials = [x for x in searched_tweets if (datetime.datetime.utcnow() - x.created_at).seconds < 3600]
    #print(len(potentials))
    targets = []
    for i in potentials:
        tar = True
        if "RT " in i.text or i.retweeted or i.user.name == 'AutoMcCree':
            tar = False
            #print("exclude " + i.text)
        if tar:
            targets.append(i)

    for k in targets:
        if k.user.screen_name == "Strandtasche":
            api.update_status("@" + k.user.screen_name + " " + "stop posting about shoelaces!", in_reply_to_status_id=k.id)
            print("")
        #print(k.text)
        #print(k.user.name + " " + k.user.screen_name)
