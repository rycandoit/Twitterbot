# Twitterbot w/Phillips Hue
A very SIMPLE bot that tracks use of specific hashtags and flashes Phillips Hue light bulbs. Thanks Edews for the initial tweepy code.

This bot uses the Python library Tweepy to access the Twitter API, so we need to first install it.

sudo pip install tweepy

It also uses phue Python library to control the Philips Hue lighting system

sudo pip install phue

Now you're all set to use the python script, you can run it with:

sudo python tweet.py

If it doesn't run, you might need to install python;

sudo apt-get install python

