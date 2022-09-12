# import required modules
import time
import tweepy
from phue import Bridge

# hue items needed
b = Bridge('192.168.2.139')
# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

# credentials to login to twitter api
consumer_key = 'place key here'
consumer_secret = 'place key here'
access_token = 'place key here'
access_secret = 'place key here'

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
try:
        api.verify_credentials()
        print("Success creating API")
        time.sleep(10)
except tweepy.TweepError as e:
        print(e.reason)

#Set hue color
redcommand =  {'transitiontime' : 1, 'bri' : 254, 'hue' : 0, 'sat' : 254}
greencommand =  {'transitiontime' : 1, 'bri' : 254, 'hue' : 25335, 'sat' : 241}
bluecommand =  {'transitiontime' : 1, 'bri' : 254, 'hue' : 46639, 'sat' : 254}
whitecommand =  {'transitiontime' : 1, 'bri' : 254, 'hue' : 34069, 'sat' : 251}

#This is where I specify which hashtags I want to track and which color I want them on. Could've named them better, but since I'm working with color, this was more fun.
blue = "covid19"
green = "corona"
red = "quarantine"

class MyStreamListener(tweepy.Stream):

    def on_status(self, status):
        for i in range(len(status.entities.get('hashtags'))): #for every tweet, it checks all hashtags to see if it matches any of the three we're looking for
            if (status.entities.get('hashtags')[i].get('text')) == blue:
                print (status.author.screen_name +  " just used "'#' + (status.entities.get('hashtags')[i].get('text')))
                b.set_light(2, bluecommand)
                time.sleep(2)
                b.set_light(2, whitecommand)

            elif (status.entities.get('hashtags')[i].get('text')) == green:
                print (status.author.screen_name + " just used "'#' + (status.entities.get('hashtags')[i].get('text')))
                b.set_light(3, greencommand)
                time.sleep(2)
                b.set_light(3, whitecommand)

            elif (status.entities.get('hashtags')[i].get('text')) == red:
                print (status.author.screen_name + " just used "'#' + (status.entities.get('hashtags')[i].get('text')))
                b.set_light(5, redcommand)
                time.sleep(2)
                b.set_light(5, whitecommand)


myStream = MyStreamListener(consumer_key, consumer_secret, access_token, access_secret)

#here is where the filter actually starts. You can change it to either a simple string for keywords, or add a @ to find whatever someone tweeted to.
print("Looking for Hashtags... " '#'+blue, '#'+green, '#'+red)
myStream.filter(track=['#'+blue, '#'+green, '#'+red])