import tweepy
import time
import bitdotio
# import psycopg2


consumer_key = 'Dyh71DNiNnqNR3vJZCuDddjYt'
consumer_secret = 'v2hdV21Srp9FNrbmOKXZ94LjEgNC6lk4OnbrzxGAKoNpp0oYc9'

access_token = '451480537-cOiesvc8QOzLefmZvK1jqudPof6o18xik03M6KuO'
access_token_secret = 'EK55sIHc8NAB7CZdRBcWvhCvQOs9HlHxeYE9Dp2AT3ZKN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=False)

# Connect to bit.io
b = bitdotio.bitdotio('BRRW_svr3AXFkgRUE8WgYcMs9NC7')


# print(b.list_repos("CasualCoder"))

# How about some database queries?
conn = b.get_connection()
cur = conn.cursor()
cur.execute('SELECT * from "CasualCoder/stock_ticker"."sp_500"')
print(cur.fetchall())

# conn = psycopg2.connect(
#     host="db.bit.io",
#     database="bitdotio",
#     port="5432",
#     user="CasualCoder_demo_db_connection",
#     password="BQwy_HTut5zbEUzs69ctUPuHs8Yy")

# cur = conn.cursor()

# cur.execute("""use database stock_ticker;""")
# cur.execute("""select count(*) from stock_ticker.twitter_tweets""")


class UserTweet:
    x = "this is from the user class"

class UserInfo:
    pass

class TweetSymbols:
    pass

p1 = UserTweet()
print(p1.x);



# Define the search term and the date_since date as variables
search_words = "PLTR"
date_since = "2021-08-05"


# public_tweets = api.search(q='$RKT', since=date_since).items(100)
# for tweet in public_tweets:
#     print(tweet.text)

#Commented out for testing
# tweets = tweepy.Cursor(api.search,
#               q=search_words + " -filter:retweets",
#               lang="en",
#               since=date_since).items(10000)

# for tweet in tweets:
#     print(tweet.user.name + "-" + tweet.user.screen_name + "-" + tweet.user.location)
    

# for tweet in tweets:
#     print(tweet.text)
