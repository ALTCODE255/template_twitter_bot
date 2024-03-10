import os
import pickle
import random
import re
import sys

import tweepy
from dotenv import load_dotenv


def initClient() -> tweepy.Client:
    env_vars = {"CONSUMER_KEY", "CONSUMER_SECRET",
                "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET"}
    if not set(os.environ).issuperset(env_vars):
        sys.exit("One or more .env variables are missing. Make sure CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET are supplied.")

    return tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )


def getRandomTweet(log: list[str]) -> str:
    filename = os.getenv("SOURCE_FILENAME", "tweets.txt")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_tweets = re.findall(
                r"^(?!#.*$)\S.*", f.read().strip("\n"), re.MULTILINE)
    except FileNotFoundError:
        sys.exit(f"Source file '{filename}' not found.")
    valid_tweets = [tweet for tweet in all_tweets if tweet not in log]
    if valid_tweets:
        random_tweet = random.choice(valid_tweets).replace("\\n", "\n")
        return random_tweet
    sys.exit(f"Not enough tweets in '{filename}'!")


def postTweet():
    try:
        with open("recent.pkl", "rb") as f:
            log = pickle.load(f)
    except FileNotFoundError:
        limit = os.getenv("STORAGE_THRESHOLD", 11)
        if not limit.isdigit() or int(limit) < 11:
            limit = 11
        log = [None]*int(limit)

    while True:
        tweet = getRandomTweet(log)
        try:
            client.create_tweet(text=tweet)
            break
        except Exception as e:
            # just in case
            if "duplicate content" in e:
                continue
            elif "text is too long" in e:
                sys.exit(f"'{tweet}' is too long to be posted!")
            print(e)
            return

    log.pop(0)
    log.append(tweet)
    with open("recent.pkl", "wb") as f:
        pickle.dump(log, f)


if __name__ == "__main__":
    os.chdir(sys.path[0])
    if load_dotenv():
        client = initClient()
        postTweet()
