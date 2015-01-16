#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
reload(sys).setdefaultencoding("utf8")

import re
import ircbot
import function
import helpcmd

# Change IRC configuration here
ircHost = "irc.freenode.net"
ircPort = 8000
botName = "bzzzt"
botPass = ""
ircChan = "#linuxba"
ircLeng = 130

# Change API here
tulingURL = "http://www.tuling123.com/openapi/api?key=b1833040534a6bfd761215154069ea58&info="
chatURL = tulingURL
jokeURL = tulingURL
maximURL = "http://api.hitokoto.us/rand?charset=utf-8"
smURL = "http://xiaofengrobot.sinaapp.com/web.php?para="
trickURL = tulingURL
weatherURL = tulingURL


bot = ircbot.ircBot(ircHost, ircPort, botName, botPass, ircChan)
bot.createConnection()

while True:
	for message in bot.receiveData():
		print message
		bot.responsePingfromServer(message)

		replies = []
		if re.search(R"PRIVMSG(.+?):\>h$", message.strip()):
			replies = helpcmd.reply()
		elif re.search(R"PRIVMSG(.+?):\>b (.+)", message):
			replies = function.webapi.chat.reply(chatURL, re.search(R"PRIVMSG(.+?):\>b (.+)", message).group(2))
		elif re.search(R"PRIVMSG(.+?):\>j$", message.strip()):
			replies = function.webapi.joke.reply(jokeURL)
		elif re.search(R"PRIVMSG(.+?):\>m$", message.strip()):
			replies = function.webapi.maxim.reply(maximURL)
		elif re.search(R"PRIVMSG(.+?):\>s (.+)", message):
			replies = function.webapi.sm.reply(smURL, re.search(R"PRIVMSG(.+?):\>s (.+)", message).group(2))
		elif re.search(R"PRIVMSG(.+?):\>u (.+)", message):
			replies = function.webapi.trick.reply(trickURL, re.search(R"PRIVMSG(.+?):\>u (.+)", message).group(2))
		elif re.search(R"PRIVMSG(.+?):\>w (.+)", message):
			replies = function.webapi.weather.reply(weatherURL, re.search(R"PRIVMSG(.+?):\>w (.+)", message).group(2))
		elif re.search(R"PRIVMSG(.+?):\>f (.+)", message):
			replies = function.fenci.reply(re.search(R"PRIVMSG(.+?):\>f (.+)", message).group(2))
		elif re.search(R"privmsg(.+?):ping\!$", message.strip().lower()):
			replies = "Pong!"
		elif re.search(R"JOIN", message.strip()):
			if re.search(R"PRIVMSG", message.strip()):
				pass
			elif re.match(r"^:([^!]+)", message).group(1) == botName:
				pass
			else:
				nickname = re.match(r"^:([^!]+)", message).group(1)
				print "<<< " + nickname
				bot.Sock.send("PRIVMSG " + ircChan + " :"  + "?ip " + nickname + "\r\n")

		if len(replies) > 0:
			nickname = re.match(r"^:([^!]+)", message).group(1)
			print "<<< " + nickname
			bot.replyMessage(replies, nickname, ircLeng)
