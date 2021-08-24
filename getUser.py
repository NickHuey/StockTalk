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

### Connect to bit.io ###
# b = bitdotio.bitdotio('BRRW_svr3AXFkgRUE8WgYcMs9NC7')
# # Create database connection (bit.io)
# conn = b.get_connection()
# cur = conn.cursor()
###

### Connect to SQLite ###
conn = sl.connect('data/stock-talk.db')
cur = conn.cursor()
#Create Tables
# with conn:
#   #twitter_tweets
#   conn.execute("""
#         CREATE TABLE twitter_tweets(
#           user_id INT8,
#           user_name TEXT,
#           screen_name TEXT,
#           create_date timestamptz(6),
#           text TEXT,
#           tweet_id INT8,
#           follower_count INTEGER,
#           profile_image VARCHAR,
#           url VARCHAR,
#           load_date datetime DEFAULT current_timestamp
#           )
#         """)
  # twitter_symbols
  # conn.execute("""
  #       CREATE TABLE twitter_symbols(
  #         user_id INT8,
  #         tweet_id INT8,
  #         symbol VARCHAR,
  #         date_loaded datetime DEFAULT current_timestamp
  #       )""")



#Output filename
output_file = "output/tweet_counts.csv"

#Field Names
fields = ["Symbol", "Volume", "Tweets"]

#Read in Ticker data
ticker_df = pd.read_csv("data/watchlist.csv")

#Setup Filter for 2M in Volume
is_2M = ticker_df["Volume"] >= 2000000

#Apply Filter to capture symbols with at least 2M in Volume
output = ticker_df[is_2M]
final = output.sort_values(by='Volume',ascending=True)

# #Commented out for testing
screen_name = "baminvestor"
tweets = api.user_timeline(screen_name)

for tweet in tweets:

    #Insert Tweets
      cur.execute('''INSERT INTO twitter_tweets VALUES (?,?,?,?,?,?,?,?,?,?)''',(tweet.user.id,tweet.user.name,tweet.user.screen_name, tweet.created_at, tweet.text, tweet.id, tweet.user.followers_count, tweet.user.profile_image_url_https, tweet.user.url, datetime.now()))
      conn.commit()
      # # print(str(tweet.user.id) + "-" + tweet.user.name + "-" + tweet.user.screen_name + "-" + str(tweet.created_at) + "-" + tweet.text)
      for symbol in tweet.entities['symbols']:
            cur.execute('''INSERT INTO twitter_symbols VALUES (?,?,?,?)''',(tweet.user.id, tweet.id, symbol['text'].upper(), datetime.now()))
            conn.commit()
      print(tweet.user.screen_name + "Created: " + str(tweet.created_at))

time.sleep(.25)  # sleep for few extra sec
