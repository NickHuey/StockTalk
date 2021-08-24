import pandas as pd

#Field Names
fields = ["Symbol", "Volume", "Tweets"]

#Read in Ticker data
ticker_df = pd.read_csv("data/nyse_081821.csv")

#Setup Filter for 2M in Volume
is_2M = ticker_df["Volume"] >= 2000000

#Apply Filter to capture symbols with at least 2M in Volume
output = ticker_df[is_2M]
final = output.sort_values(by='Volume',ascending=True)
final['Symbol'] =  '$' + final['Symbol']
print(final['Symbol'].tolist())
