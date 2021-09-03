-- SQLite
SELECT symbol, first_value(price) over (partition by symbol order by date_loaded desc) as latest_price, count(tweet_id) as tweet_count
FROM twitter_symbols
where date_loaded >='2021-08-23'
group by symbol
order by tweet_count desc
