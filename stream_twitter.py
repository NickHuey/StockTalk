import tweepy
import time
import bitdotio
from datetime import datetime
import pandas as pd
import sqlite3 as sl

# import psycopg2


#Connect to bit.io

consumer_key = 'Dyh71DNiNnqNR3vJZCuDddjYt'
consumer_secret = 'v2hdV21Srp9FNrbmOKXZ94LjEgNC6lk4OnbrzxGAKoNpp0oYc9'

access_token = '451480537-cOiesvc8QOzLefmZvK1jqudPof6o18xik03M6KuO'
access_token_secret = 'EK55sIHc8NAB7CZdRBcWvhCvQOs9HlHxeYE9Dp2AT3ZKN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth
  ,wait_on_rate_limit=True
  ,wait_on_rate_limit_notify=True)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status._json["user"]["screen_name"] + " - " + str(status._json["user"]["followers_count"]) )


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['$PLTR','$AMC','$AMD'], is_async=True)

