# Twitterbot w/Phillips Hue
A very SIMPLE bot that tracks use of specific hashtags and flashes Phillips Hue light bulbs. Thanks Edews for the initial tweepy code.

This bot uses the Python library Tweepy to access the Twitter API, so we need to first install it.

sudo pip install tweepy

It also uses phue Python library to control the Philips Hue lighting system

sudo pip install phue

Get Bridge and Bulb Info

Step 1
First make sure your Phillips Hue bridge is connected to your network and is functioning properly. Test that the smartphone app can control the lights on the same network.

Step 2
Log into your wireless router and look for Philips hue IP address in the DHCP table.

Step 3
Once you have the bridge IP address load the hue API debug tool by visiting the following address in your web browser.
https://<bridge ip address>/debug/clip.html
You should see an interface like this.

Step 4
Set the URL to /api
Put the following in the message body
{"devicetype":"my_hue_app#iphonetest"}
Go and press the button on the bridge and then press the POST button and you should get a success response like below.
Copy the username

Step 5
Set the URL to https://<bridge ip address>/api/<username>/lights
press the GET button
You should get a JSON response with all the lights in your system and their names, status and current color. We will need this info for determining bulb id numbers and if you want to change the scripts colors (just run step 5 after you set your colors via phone app)

Edit script
sudo nano tweet.py

Add your bridges ip on line 8

Add in your twitter api keys on lines 13-16

Change line 46 to match the bulb id and color you want to use when hashtag is covid19. 2 being my bulb id
b.set_light(2, bluecommand)
Change line 48 to the same bulb id and color you want the bulb to return to after hashtag is covid19.
b.set_light(2, whitecommand)

Change line 52 to match the bulb id and color you want to use when hashtag is corona. 3 being my bulb id
b.set_light(3, greencommand)
Change line 54 to the same bulb id and color you want the bulb to return to after hashtag is corona.
b.set_light(3, whitecommand)

Change line 58 to match the bulb id and color you want to use when hashtag is quarantine 5 being my bulb id
b.set_light(5, redcommand)
Change line 60 to the same bulb id and color you want the bulb to return to after hashtag is quarantine.
b.set_light(5, whitecommand)

Exit nano CTRL-X, y for save, enter

Now you're all set to use the python script, you can run it with:

sudo python tweet.py

If it doesn't run, you might need to install python;

sudo apt-get install python

