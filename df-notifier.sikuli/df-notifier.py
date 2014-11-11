# author: deathforge@gmail.com
# date: 11/09/2014
# df-notifier sends a message to your phone or executes a command when your dungeon or battleground is ready

import httplib, urllib, ConfigParser

#loop var
looper = 1

#setup settings
config = ConfigParser.RawConfigParser()
if config.read("config.cfg"):
    config.read('config.cfg')
    pushover_token = config.get('Pushover', 'pushover_token')
    user_token = config.get('Pushover', 'user_token')
    command = config.get('General', 'command')
else:
    file = open('config.cfg', 'w+')
    pushover_token = input("Enter your pushover token:")
    user_token = input("Enter your pushover user token:")
    config.add_section('Pushover')
    config.set('Pushover', 'pushover_token', pushover_token)
    config.set('Pushover', 'user_token', user_token)
    config.add_section('General')
    config.set('General', 'command', 'Enter command here')
    with open('config.cfg', 'wb') as configfile:
        config.write(configfile)

#pushover function
def sendmsg(msg):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": pushover_token,
    "user": user_token,
    "message": msg,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

#keep looping til we find what we need
while looper == 1:
    dungeon = exists("1415492721612.png",0)
    pvp = exists("1415493216484.png",0)
    if dungeon:
        if command is not "Enter command here":
            run(command)
        sendmsg("Your dungeon is ready.")
        looper = 0
        break
    if pvp:
        if command is not "Enter command here":
            run(command)
        sendmsg("Your battleground is ready.")
        looper = 0
        break