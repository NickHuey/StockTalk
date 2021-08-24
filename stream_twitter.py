import tweepy
import time
import bitdotio
from datetime import datetime
import pandas as pd
import sqlite3 as sl
import yfinance as yf
# import psycopg2


#Connect to bit.io
print('Collecting Data...')

consumer_key = 'Dyh71DNiNnqNR3vJZCuDddjYt'
consumer_secret = 'v2hdV21Srp9FNrbmOKXZ94LjEgNC6lk4OnbrzxGAKoNpp0oYc9'

access_token = '451480537-cOiesvc8QOzLefmZvK1jqudPof6o18xik03M6KuO'
access_token_secret = 'EK55sIHc8NAB7CZdRBcWvhCvQOs9HlHxeYE9Dp2AT3ZKN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth
  ,wait_on_rate_limit=True
  ,wait_on_rate_limit_notify=True)

### Connect to SQLite ###
# conn = sl.connect('data/stock-talk.db')
# cur = conn.cursor()

#Field Names
fields = ["Symbol", "Volume", "Tweets"]

#Read in Ticker data
ticker_df = pd.read_csv("data/nyse_081821.csv")

#Setup Filter for 2M in Volume
is_2M = ticker_df["Volume"] >= 5000000

#Apply Filter to capture symbols with at least 2M in Volume
output = ticker_df[is_2M]
final = output.sort_values(by='Volume',ascending=True)
final['Symbol'] = '$' + final['Symbol']
symbol_list = final['Symbol'].tolist()


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        ### Connect to SQLite ###
        conn = sl.connect('data/stock-talk.db')
        cur = conn.cursor()
        tweet = status._json

        if not tweet["retweeted"] and 'RT @' not in tweet["text"] and tweet['lang']=="en":
          print(tweet["user"]["screen_name"] + " - " + str(tweet["retweeted"]) + " - " + tweet["text"] )
          #Insert Tweets
          cur.execute('''INSERT INTO twitter_tweets VALUES (?,?,?,?,?,?,?,?,?,?)''',(tweet["user"]["id"],tweet["user"]["name"],tweet["user"]["screen_name"], tweet["created_at"], tweet["text"], tweet["id"], tweet["user"]["followers_count"], tweet["user"]["profile_image_url_https"], tweet["user"]["url"], datetime.now()))
          conn.commit()
          for symbol in tweet["entities"]["symbols"]:
              try:
                ticker = yf.Ticker(symbol["text"].upper())
                # print(symbol["text"].upper() + " - " + str(ticker.info['currentPrice']))
                cur.execute('''INSERT INTO twitter_symbols VALUES (?,?,?,?,?)''',(tweet["user"]["id"], tweet["id"], symbol["text"].upper(), datetime.now(),ticker.info['regularMarketPrice']))
                conn.commit()
              except KeyError:
                pass

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

print(symbol_list)
myStream.filter(track=symbol_list, is_async=True)

