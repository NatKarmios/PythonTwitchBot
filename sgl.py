"""
   === STEAM GAME LIST RETRIEVER ===

This is purely experimental - you'll have to manually change bot.py in order to integrate this in with the bot.

This was intended for use with Strawpoll creation (in sp.py), but this idea was scrapped, because Strawpoll allows a
maximum of 30 options, and of course, many people have more than 30 Steam games.

"""

import requests
import json

# You need to use your own values here - these are just placeholders
apikey = '1111A11A11111A11111A1A11A1AAA1A1'
steamid = '11111111111111111'


def getownedgames(apikey, steamid):
    url = ('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
           '?key={}&steamid={}&include_appinfo=1'.format(apikey, steamid))

    return json.loads(requests.get(url).content.decode())['response']['games']