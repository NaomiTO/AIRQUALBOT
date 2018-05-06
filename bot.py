# This is merging examples from tweepy documentation and:
# https://github.com/bomeara/purpleairpy/blob/master/thingspeakexample.py
# example from https://github.com/mchwalisz/thingspeak/blob/master/examples/pull.py
# original repo: https://github.com/mchwalisz/thingspeak/
# keys from first sensor at https://www.purpleair.com/json

import tweepy
import thingspeak

# there is a secrets.py file that has the keys
from secrets import CONSUMER_KEY
from secrets import CONSUMER_SECRET
from secrets import ACCESS_KEY
from secrets import ACCESS_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

channel_id = 358829 # Change for your sensor
read_key    = 'HMKW1CQN5IHL5NUD' # West Knoxville, TN sensor

channel = thingspeak.Channel(id=channel_id,api_key=read_key, fmt='txt')

# http://aqicn.org/faq/2013-09-09/revised-pm25-aqi-breakpoints/
# conversion chart from PM2.5 to quality
# 0-12: Good
# 12.1-35.4: Moderate
# 35.5-55.4: Unhealthy for sensitive groups
# 55.5-150.4: Unhealthy
# 150.5-250.4: Very Unhealthy
# 250.5-500: Hazardous

Air_Quality = "Unknown"

try:
    # Get the last 2 results from field 2 of your channel
    #print(channel.get_field(field='field2', options = {'results': 2}))
    # Get the age of the last data in field 2 of your channel in seconds
    #print(channel.get_last_data_age(field='field2'))
    # Get the last data in field 2 of your channel
    #print(channel.get_field_last(field='field2'))
    # example tweet: "Particles in the air: blank. Particles can cause blank. If you are blank sensitive be careful. Like golf, the lower the number the better."
    Particles = float(channel.get_field_last(field='field2'))
    if Particles < 12.1:
        Air_Quality = "Good air quality today. It might be nice to play outside. Fun Fact: Like golf, the lower the number, the better the score."
    elif Particles < 35.5:
        Air_Quality = "The air quality is okay... could be better. Moderate air, still quite fair."
    elif Particles < 55.5:
        Air_Quality = "If you are sensitive be careful, the air is unhealthy for you."
    elif Particles < 150.5:
        Air_Quality = "The air is unhealthy, try to stay indoors more."
    elif Particles < 250.5:
        Air_Quality = "Stay inside as much as possible, the air is very unhealthy. Fact: Too many particles can make it difficult to breathe."
    elif Particles < 500.1:
        Air_Quality = "WARNING! Air is hazardous. Stay inside!"
    api.update_status(Air_Quality)
except:
    raise
    print("connection failed")
