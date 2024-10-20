import re
import sys
import glob
import os
import random

from bot import loadConfig


def getNumTweets(filename: str) -> int:
    return len(getTweets(filename))


def getTweets(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_tweets = [
                tweet.replace("\\n", "\n")
                for tweet in re.findall(
                    r"^(?!#.*$)\S.*", f.read().strip("\n"), re.MULTILINE
                )
            ]
        exceeding_tweets = [tweet for tweet in all_tweets if len(tweet) > 280]
        if exceeding_tweets:
            print(
                f"Warning: The following tweets exceed 280 characters:\n- "
                + "\n- ".join(exceeding_tweets)
            )
        return all_tweets
    except FileNotFoundError:
        print(f"Source file '{filename}' not found.")


def getRandomTweet(filename: str) -> str:
    return random.choice(getTweets(filename))


if __name__ == "__main__":
    os.chdir(sys.path[0])
    config_dict = loadConfig()
    if len(sys.argv) == 1 or sys.argv[1] == "help":
        print(
            "Commands:\n\
                  - help - displays this command\n\
                  - random <file path> - selects a random valid tweet from the specified file.\n\
                  - countall - counts the number of valid tweets in every source file in tweets.\n\
                  - count <file path> - counts the number of valid tweets in a specified text file given a filepath.\n\
                  - list <file path> - displays list of all valid tweets found in a specified text file."
        )
    elif len(sys.argv) == 2 and sys.argv[1] == "countall":
        files = glob.glob("tweets/*.txt")
        for source in files:
            print(
                "Number of Tweets in",
                source + ":",
                getNumTweets(source),
            )
    elif len(sys.argv) >= 3:
        match sys.argv[1]:
            case "list":
                print(f"List of Valid Tweets in {sys.argv[2]}:", getTweets(sys.argv[2]), sep="\n")
            case "count":
                print(
                    f"Number of Valid Tweets in {sys.argv[2]}:",
                    getNumTweets(sys.argv[2]),
                )
            case "random":
                print(f"Random Tweet from {sys.argv[2]}:", getRandomTweet(sys.argv[2]), sep="\n")
