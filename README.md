## Nameless's Twitter Bot Template

### Requirements

1. A host machine or server (e.g. a Raspberry Pi) that can be scheduled to run a Python script on an interval
2. Python 3.8+
3. [Tweepy](https://pypi.org/project/tweepy/) and [python-dotenv](https://pypi.org/project/python-dotenv/) (install using `pip install -r requirements.txt`)
4. A [Twitter App](https://developer.twitter.com/en/portal/) that uses Twitter API v2 and has "Read and write" user authentication app permissions
5. At least 12 different possible tweets for the script to choose from. The more, the merrier.

### Instructions

1. [Download](https://github.com/ALTCODE255/template_twitter_bot/archive/refs/heads/master.zip) this Github repository and unzip it.
2. Paste your Twitter API keys in the `.env` file.
   1. (Optional) Set `STORAGE_THRESHOLD` to an integer higher than `11` for higher "randomness".
      1. This variable indicates how many recent tweets the program stores (to avoid duplicate tweets).
   2. (Optional) Change `SOURCE_FILENAME` from `tweets.txt` to an alternative filename of your desire. Make sure to rename the existing `tweets.txt` file if you do this.
      1. This variable indicates where you store your pool of potential tweets.
3. In the `tweets.txt` file (or another name if you changed it in step 2), fill the file with tweets according to the guidelines specified.
   1. If you changed `STORAGE_THRESHOLD` in step 2, make sure the number of tweets you enter in this file is _higher_ than `STORAGE_THRESHOLD`.
4. Use a task scheduler of your choice to schedule your machine to **run the Python file** however often you want your Twitter bot to tweet.
   1. Ex. In crontab, you'd put `30 * * * * python path\to\folder\bot.py` to have the script run every hour at the :30 minute mark.
5. That's it!

**NOTE:** Do _not_ delete the `recent.pkl` file from the folder unless you wish to reset the log of recent tweets. It is necessary for keeping a record of the most recently generated tweets to avoid being throttled by Twitter for duplicate tweets.

**Tip:** If you want to know how many tweets are counted in your source file, run `python util.py count`. If you want to know _which_ tweets are being counted from your source file, run `python util.py list`. For both, run `python util.py` (no arguments).
