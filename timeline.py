import tweepy
import time
import pandas as pd
import csv
import json

consumer_key = 'Dyh71DNiNnqNR3vJZCuDddjYt'
consumer_secret = 'v2hdV21Srp9FNrbmOKXZ94LjEgNC6lk4OnbrzxGAKoNpp0oYc9'

access_token = '451480537-cOiesvc8QOzLefmZvK1jqudPof6o18xik03M6KuO'
access_token_secret = 'EK55sIHc8NAB7CZdRBcWvhCvQOs9HlHxeYE9Dp2AT3ZKN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

screen_name = "thecasualcoder"
user = api.get_user(screen_name)
statuses = api.user_timeline(screen_name)
status = statuses[0]
json_str = json.dumps(status._json)

f = open("output/tweet_by_user.json","a")
f.write("[")
# print (json_str)
for status in statuses:
    print (json.dumps(status._json))
    f.write(json.dumps(status._json)+",")
f.write("]")
