#Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key='**********************'
consumer_secrate='**********************'

access_token='**********************'
access_token_secrate='**********************'

auth=tweepy.OAuthHandler(consumer_key,consumer_secrate)
auth.set_access_token(access_token,access_token_secrate)
api=tweepy.API(auth)

hash_tag=input("enter the hash tag to search")
number=input("enter number of tweets you want to see")

tweets=api.search(hash_tag,lang="en",count=number,tweet_mode="extended")

#print tweets

for tweet in tweets:
    print("________________")
    print(tweet.full_text)
    print("________________")
