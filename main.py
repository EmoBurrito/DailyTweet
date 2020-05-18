#!/usr/bin/env/ python3
from datetime import date
from twython import Twython

Twython(
    'api key',
    'api secret key',
    'access token',
    'access token secret'
).update_status(status="[Day {}] I will tweet @DevEjm everyday until they fix their bot.".format((date.today() - date(2020, 5, 15)).days)
