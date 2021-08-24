import yfinance as yf
import sqlite3 as sl

### Connect to SQLite ###
conn = sl.connect('data/stock-talk.db')
cur = conn.cursor()

cur.execute('select distinct symbol from twitter_symbols order by symbol')
for symbol in cur.fetchall():
      # print(symbol[0])
      ticker = yf.Ticker(symbol[0])

      hist = ticker.history(period="max")
      print(symbol[0]  + " - " + str(ticker.info['regularMarketPrice']))
