#!/usr/bin/env python3

# Tests given API secrets against Twitter with basic timeline read

import tweepy

consumer_key = ''
consumer_secret = ''
secret = ''
key = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
