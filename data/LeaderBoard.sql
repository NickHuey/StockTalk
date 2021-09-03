with detail as (
select symbol.user_id
, tweet.screen_name
, tweet.user_name
, tweet.profile_image
, tweet.url
, max(tweet.followers) as followers
, symbol.tweet_id
, symbol.symbol
, symbol.date_loaded
, price as tweet_price 
, "Last Sale" as today_price
, ((cast(replace("Last Sale",'$','') as float) - cast(price as float))/cast(price as float))*100 as prcnt_diff
, Sector
, Industry
from twitter_symbols symbol 
join nasdaq_screener nas
on symbol.symbol = nas.symbol
join (select user_id, user_name, screen_name, profile_image, url, max(follower_count) as followers from twitter_tweets group by user_id, user_name, profile_image, url, screen_name having followers >5000) as tweet
on symbol.user_id = tweet.user_id
-- where symbol.user_id = 15281391
group by symbol.user_id
, tweet.screen_name
, tweet.profile_image
, tweet.user_name
, tweet.url
, symbol.tweet_id
, symbol.symbol
, symbol.date_loaded
, price
, "Last Sale"
, Sector
, Industry
order by symbol.date_loaded)

select screen_name, followers, profile_image, url, user_name
, avg(prcnt_diff) as avg_performance
, count(distinct tweet_id) as tweets
, count(distinct symbol) as symbols
, max(date_loaded) as last_tweet
from detail
where (JulianDay(CURRENT_DATE)-JulianDay(date_loaded)) <=7
group by screen_name, followers
order by avg_performance desc