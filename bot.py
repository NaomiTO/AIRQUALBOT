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

channel_id = 411751 # Change for your sensor
read_key    = 'BVJS8JTJ7161UVEB'

channel = thingspeak.Channel(id=channel_id,api_key=read_key)




try:
    # Get the last 2 results from field 1 of your channel
    print(channel.get_field(field='field1', options = {'results': 2}))
    # Get the age of the last data in field 1 of your channel in seconds
    print(channel.get_last_data_age(field='field1'))
    # Get the last data in field 1 of your channel
    print(channel.get_field_last(field='field1'))
    # example tweet: "Particles in the air: blank. Particles can cause blank. If you are blank sensitive be careful. Like golf, the lower the number the better."
    api.update_status("Too many particles in the air can cause many problems, and make it diffucult to breathe" + channel.get_field_last(field='field1'))
except:
    raise
    print("connection failed")
