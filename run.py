#!/usr/bin/env python3

import ircbot

ircHost = "irc.freenode.net"
ircPort = 6666
botName = "bots-xiaoice"
botPass = ""
ircChan = "#jolla-cn"



bot = ircbot.ircBot(ircHost, ircPort, botName, botPass, ircChan)
bot.start()
