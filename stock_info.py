from polygon import RESTClient

key = 'C1zcF27LP200p027JUmvAZgpwh_VVl8f'

with RESTClient(key) as client:
    resp = client.ticker_details("PLTR")
    print(resp.description)
