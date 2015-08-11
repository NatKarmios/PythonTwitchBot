"""
    === THE BOT ===

This is the bot's main code - you'll be running this .py file.

"""

# ----------------------------------------------------------------------------------------------------------------------

"""
   --- Helper Functions ---

Don't touch these.

"""
def send(clientSocket, msg):
    if len(message) > 0:
        clientSocket.sendall((msg + "\n").encode("utf-8"))


def chat(msg):
    print(cfg.NICK + ": " + msg)
    send(s, ('PRIVMSG {0} :{1}'.format(chan, msg)))


# ----------------------------------------------------------------------------------------------------------------------

"""
   --- Chat Functions ---

These are the functions that handle various things in chat.

Feel free to add to these if you know what you're doing - make sure that your functions only take two strings as
parameters - in the examples below, 'nick' is the sender of the message that triggered the command, and 'msg' is the
message sent, command and all.

"""

def test(nick, msg):
    chat("/me is functional!")


def reply(nick, msg):
    chat("/me - " + msg.strip("!reply "))


def poll(nick, msg):
    if nick not in cfg.MODS:
        return
    ls = re.findall('"(.+?)"', msg)
    if len(ls) < 2:
        chat('/me - Correct usage: !poll "Poll Title" "Option 1" "Option 2" etc (with quotation marks).')
    else:
        chat('/me - The poll "' + ls[0] + '" has been started at ' + sp.create(ls[0], ls[1:]))

# ----------------------------------------------------------------------------------------------------------------------

"""
   --- Setup ---

Don't touch any of this, either.
"""

import cfg
import socket
import re
import time
import sp

answer = ""

print("Available channels:")
for i in range(len(cfg.CHAN)):
    print("  %s: %s" % (str(i + 1), cfg.CHAN[i]))

while answer not in list(map(str, range(1, len(cfg.CHAN) + 1))):
    answer = input("\nEnter your desired channel's number: ")

chan = "#" + cfg.CHAN[int(answer) - 1]
print("Channel has been set to " + chan)

s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(chan).encode("utf-8"))

# ----------------------------------------------------------------------------------------------------------------------

"""
   --- General Commands ---

If you don't know what you're doing, *do not touch this*.

After defining a command in the above section, this is the easy way to get the bot to recognise it. The dictionary
keys here are regex patterns that are used against any messages received, and values are the names of the respective
function (without parentheses).

If you aren't very good with regex, here is a template for a basic command with no parameters:
  "^!command\s*$"
Replace command with your command name.

"""

cmds = {
    "^!test\s*$": test,
    "^!reply\s*": reply,
}

# ----------------------------------------------------------------------------------------------------------------------

"""
   --- Channel-Specific Commands ---

chan_cmds is a nested dictionary - keys are channel names (as defined in cfg.py) and values are dictionaries similar to
cmds, with a regex pattern and the function's parentheses-less name.

Channel-specific commands *will override general commands*, if a channel-specific command matched first.

"""

chan_cmds = {
    "debugthis": {
        "^!poll\s*": poll
    }
}

# ----------------------------------------------------------------------------------------------------------------------


def parse(nick, msg):
    for i in chan_cmds[chan[1:]]:
        if re.search(i, msg, flags=re.I):
            chan_cmds[chan[1:]][i](nick, msg)
            return

    for i in cmds:
        if re.search(i, msg, flags=re.I):
            cmds[i](nick, msg)
            return

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        username = re.search(r"\w+", response).group(0)  # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)

        parse(username, message)

    time.sleep(0.3)
