import re
import os
import sys
from dotenv import load_dotenv


def getNumTweets(filename) -> int:
    return len(getTweets(filename))


def getTweets(filename) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_tweets = re.findall(
                r"^(?!#.*$)\S.*", f.read().strip("\n"), re.MULTILINE)
        return all_tweets
    except FileNotFoundError:
        sys.exit(f"Source file '{filename}' not found.")


if __name__ == "__main__":
    load_dotenv()
    filename = os.getenv("SOURCE_FILENAME", "tweets.txt")
    if len(sys.argv) == 2:
        if sys.argv[1] == "count":
            print(f"Number of Valid Tweets in {filename}:",
                  getNumTweets(filename))
        elif sys.argv[1] == "list":
            print(f"List of Valid Tweets in {filename}:", getTweets(filename))
        else:
            print("Invalid argument. Valid arguments are 'count' or 'list'.")
    else:
        print(f"List of Valid Tweets in {filename}:", getTweets(filename))
        print(f"Number of Valid Tweets in {filename}:",
              getNumTweets(filename))
