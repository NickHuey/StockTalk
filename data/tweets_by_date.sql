-- SQLite
SELECT user_id, user_name, screen_name, create_date, text, load_date
FROM twitter_tweets
order by load_date desc;
