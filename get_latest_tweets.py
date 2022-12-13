import tweepy
import pandas as pd
import time

consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER KEY'
access_token = 'ACCESS TOKEN'
access_token_secret = 'ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []


def query_to_csv(text_query, count):
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=text_query).items(count)
        tweets_list = [[tweet.id, tweet.created_at, tweet.text] for tweet in tweets]

        # tweet information
        tweets_df = pd.DataFrame(tweets_list, columns=['ID', 'Datetime', 'Text'])

        tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index=False)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


# X is number of tweets to be retrieved
text_query = 'YOUR QUERY'
count = X

query_to_csv(text_query, count)
