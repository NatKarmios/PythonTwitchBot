"""
   === BOT CONFIGURATION ===

This file is used to define the settings for the bot.

These are the most essential variables for the bot's connection, so if something goes wrong, it's probably in here!

"""

# the Twitch IRC server
HOST = "irc.twitch.tv"

# the IRC port
PORT = 6667

# your Twitch account username - all lowercase (this one is an example - you need to change it yourself
NICK = "botkarmios"

# your Twitch OAuth token - (this is an example - you have to use your OAuth key, found using http://twitchapps.com/tmi/
PASS = "oauth:1a1aa1aa11111aa1a1a11aaaaa1a11"

# the list of channels that your bot can join - all lowercase
CHAN = ["debugthis", "dr4xell"]

# a dictionary showing moderators for your bot - keys = channel names, values = list of usernames
MODS = {
    "debugthis": ["natkarmios", "philz0ne", "debugthis", "nythie"],
    "dr4xell": ["natkarmios"]
}

# this is just for vanity commands - put your username here if you want
OWNER = "NatKarmios"