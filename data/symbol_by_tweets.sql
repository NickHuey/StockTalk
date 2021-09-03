-- SQLite
SELECT symbol, count(tweet_id) as tweets
FROM twitter_symbols
where date_loaded >='2021-09-03'
group by symbol
order by tweets desc;
