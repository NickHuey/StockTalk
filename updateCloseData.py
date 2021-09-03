import pandas as pd
import sqlite3 as sl


#Field Names
# fields = ["Symbol", "Volume", "Tweets"]

#Read in Ticker data
ticker_df = pd.read_csv("data/nyse_close_082321.csv")

#Setup Filter for 2M in Volume
is_2M = ticker_df["Volume"] >= 5000000

#Apply Filter to capture symbols with at least 2M in Volume
output = ticker_df[is_2M]
final = output.sort_values(by='Volume',ascending=True)
output = final.loc[:,['Symbol','Last Sale']]
final['Symbol'] = '$' + final['Symbol']
symbol_list = final['Symbol']

for ind in output.index:
      print(output['Symbol'][ind], output['Last Sale'][ind])
