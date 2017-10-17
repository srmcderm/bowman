#import tweepy and app keys

import tweepy
from textblob import TextBlob
from keys import *

#authenticate using OAuth

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

public_tweets = api.search('Dogs')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)