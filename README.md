# AIRQUALBOT
An air quality bot for twitter.

/usr/local/bin/python3 bot.py

Demo at https://twitter.com/airqualitydemo

To run app use information from the secrets file secrets.py (that you have to make). Info from creating a twitter app.

CONSUMER_KEY = 'consumkey'
CONSUMER_SECRET = 'consumsecret'
ACCESS_KEY = ' ACCESSkey'
ACCESS_SECRET = ' accesssecret'


for demo, run locally. Using a crontab

0 7 * * * /usr/local/bin/python3 /Users/naomi/Documents/GitHub/AIRQUALBOT/bot.py
0 12 * * * /usr/local/bin/python3 /Users/naomi/Documents/GitHub/AIRQUALBOT/bot.py
0 19 * * * /usr/local/bin/python3 /Users/naomi/Documents/GitHub/AIRQUALBOT/bot.py
