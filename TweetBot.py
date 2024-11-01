import tweepy
import random


class Bot:
    def __init__(self, label: str, credentials: dict[str, str], tweets: list[str]):
        self.label = label # for debugging 
        self.client = self.initClient(credentials)
        self.tweets = tweets

    def initClient(self, credentials: dict[str, str]) -> tweepy.Client:
        return tweepy.Client(
            consumer_key=credentials["CONSUMER_KEY"],
            consumer_secret=credentials["CONSUMER_SECRET"],
            access_token=credentials["ACCESS_TOKEN"],
            access_token_secret=credentials["ACCESS_TOKEN_SECRET"],
        )

    def getRandomTweet(self, log: list[str]) -> str:
        available_tweets = [tweet for tweet in self.tweets if tweet not in log]
        random_tweet = random.choice(available_tweets)
        return random_tweet

    def postTweet(self, log: list[str]):
        tweet = self.getRandomTweet(log)
        try:
            self.client.create_tweet(text=tweet)
            log.pop(0)
            log.append(tweet)
        except tweepy.Forbidden as error:
            if "duplicate content" in str(error):
                print(f"[{self.label}] Error! Duplicate content found: \"{tweet}\". Try increasing your storage_threshold config value!")
            else:
                print(f"[{self.label}]", error)
        except tweepy.TooManyRequests as error:
            print(f"[{self.label}]", error)