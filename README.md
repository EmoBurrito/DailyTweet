# DailyTweet
A simple script to [tweet the same message everyday with a slight variation](https://twitter.com/EmoBurrito2).

## Okay, but why?
I used to live with someone who coded as a hobby and has a fondness for over-engineering things. They explained to me that they wanted to write a Twitter bot that would tweet two others who have not worked together everyday until they collaborate (see user in tweets). Being three drinks deep and a professional code monkey, I figured it likely wasn't difficult and began to explain how I would do it. They respectfully declined my explanation on the grounds that they wanted to pioneer this project on their own as a learning experience, which I fully understood and was here should they need help.

Each day that I came home from work, they had a new plan, all of which with slightly more successful than the last albeit much heavier and complicated, like a digital Rube Goldberg machine. Unfortunately, it never reliably functioned so I have come up with how I would make such a thing and posting it publicly.

## And what did you gain?
Minor amusement for little under an hour while drinking, akin to that of a child with a pinwheel. Now, it is simply a waiting game to see how long it takes them to fix their bot.

## How do I do the same?
1. Get a [developer account on Twitter](https://developer.twitter.com/en/apply-for-access). You will need an API key, API secret key, access token, and access token secret.
2. Clone this repo to a machine with Python3.
3. Modify `main.py` to use your Twitter keys. Change the date to the day before you wish to start. For example, if your first tweet is on May 16, 2020, set this to be May 15, 2020 which will result in the tweet saying "Day 1".
4. Set up a crontab entry to run `engage_harassment.sh`, which will set up a virtual environment, install requirements, and post your tweet.
5. Go to the Winchester, have a nice cold pint, and wait for all this to blow over.
