import tweepy
import time
import pandas as pd
import csv

consumer_key = 'Dyh71DNiNnqNR3vJZCuDddjYt'
consumer_secret = 'v2hdV21Srp9FNrbmOKXZ94LjEgNC6lk4OnbrzxGAKoNpp0oYc9'

access_token = '451480537-cOiesvc8QOzLefmZvK1jqudPof6o18xik03M6KuO'
access_token_secret = 'EK55sIHc8NAB7CZdRBcWvhCvQOs9HlHxeYE9Dp2AT3ZKN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

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
# print(output.sort_values(by='Volume',ascending=False).head(100))
# print(final["Symbol"].head(10))

# with open(output_file, 'w') as csvfile:

  #Writer object
  # csvwriter = csv.writer(csvfile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #Write fields
  # csvwriter.writerow(fields)
f = open("output/tweet_counts.csv","a")


for index, row in final.iterrows():
    print(row['Symbol'],row['Volume'])
    volume = row['Volume']
    search_words = '$' + row['Symbol']
    date_since = "2021-07-14"
      # print (search_words)

      # csvwriter.writerows([row['Symbol']])

      # public_tweets = api.search(q=search_words, since=date_since).items(100)

      # for tweet in public_tweets:
      #     print(tweet.text)
    tweets = tweepy.Cursor(api.search,
                        q=search_words + " -filter:retweets",
                        lang="en",
                        since=date_since).items(10000)
    f.write(search_words + "," + str(volume) + "," + str(len([tweet.id for tweet in tweets])) + "\n" )
      # # print (search_words)
      # print (search_words + ' ' + str(volume) + ' ' + str(len([tweet.id for tweet in tweets])))
f.close()
