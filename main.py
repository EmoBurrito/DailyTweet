#!/usr/bin/env/ python3
from datetime import date
from twython import Twython

# Set this to be one day before your first day
# Example: if your first tweet is on May 16, 2020, set this to be May 15, 2020 which will result in the tweet saying "Day 1"
date_start = date(2020, 5, 15)
date_current = date.today()
status = "[Day {}] ".format((date_current - date_start).days)

if date_start.month == date_current.month and date_start.day == date_current.day - 1:
	status = "{}{}".format(status, "Happy {} year anniversary, @DevEjm! Fix your bot.".format(date_current.year - date_start.year))
else:
	status = "{}{}".format(status, "I will tweet @DevEjm everyday until they fix their bot.")

Twython(
    'api key',
    'api secret key',
    'access token',
    'access token secret'
).update_status(status=status)
