## Nameless' Twitter Bot Template

### Requirements

1. A host machine or server (e.g. a Raspberry Pi) that can be scheduled to run a Python script on an interval
2. Python 3.8+
3. [Tweepy](https://pypi.org/project/tweepy/) and [jsonschema](https://pypi.org/project/jsonschema/) (install both using `pip install -r requirements.txt`)
5. A [Twitter App](https://developer.twitter.com/en/portal/) that uses Twitter API v2 and has "Read and write" user authentication app permissions
6. At least 12 different possible tweets for the script to choose from. The more, the merrier.

### Instructions

1. [Download](https://github.com/ALTCODE255/template_twitter_bot/archive/refs/heads/master.zip) this Github repository and unzip it.
2. Change `anyNameHere` to anything you want. This is how the script identifies the bot.
   1. Note: if you change this later on, you will lose the bot's recent tweets log. You'll want to delete the `recent.pkl` file and let it regenerate itself.
3. Paste your Twitter API keys in the `config.json` file.
   1. (OPTIONAL) Set `storage_threshold` to an integer higher than `11` for higher "randomness".
      1. This variable indicates how many recent tweets the program stores (to avoid duplicate tweets).
   2. (OPTIONAL) Change `tweets/tweetsFile.txt` to a different path or filename (relative or absolute OK).
      1. This variable indicates where you store your pool of potential tweets.
4. In the `tweetsFile.txt` file located in the `tweets` folder (or other folder, if you changed it in step 3), fill the file with tweets according to the guidelines specified.
   1. If you changed `storage_threshold` in step 3, make sure the number of tweets you enter in this file is _higher_ than `storage_threshold`.
5. Use a task scheduler of your choice to schedule your machine to **run the Python file** however often you want your Twitter bot to tweet.
   1. Ex. In crontab, you'd put `30 * * * * python path\to\folder\bot.py` to have the script run every hour at the :30 minute mark.
6. (OPTIONAL) If you have multiple Twitter bots you want to run:
   1. Create a new `.txt` file for your new bot's source of tweets. Name it and place it whatever you like, but keep this filename and path in mind.
   2. Add a new section to the `config.json` file to set up and configure your new bot (see `config-multiple.json` for syntax) in the same way you did in step 3.
   3. Do this for however many bots you'd like to include.
7. That's it!

**NOTE:** Do _not_ delete the `recent.pkl` file from the folder unless you wish to reset the log of recent tweets. It is necessary for keeping a record of the most recently generated tweets to avoid being throttled by Twitter for duplicate tweets.

**Tip:** The `util.py` script has a few useful utilities to count the number of or list the valid tweets in your file(s). Run `python util.py help` to see the list of commands, and `python util.py <command>` to run a command.
