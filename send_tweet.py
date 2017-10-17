#import tweepy and app keys

import tweepy
from keys import *

#authenticate using OAuth

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

#update status with text
api.update_status("I'm sending this thru python, hello boredom")


