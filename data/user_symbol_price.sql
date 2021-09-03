-- SQLite
SELECT twt.user_id, user_name, screen_name, sym.symbol, sym.price, twt.load_date
FROM twitter_tweets twt
JOIN twitter_symbols sym
on twt.tweet_id = sym.tweet_id and twt.user_id = sym.user_id
order by twt.user_id, twt.load_date
