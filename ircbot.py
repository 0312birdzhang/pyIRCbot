#-*- encoding: utf-8 -*-

import sys
reload(sys).setdefaultencoding("utf8")

import socket
import time


class ircBot:

	def __init__(self, host, port, nick, password, channel):
		self.Host = host
		self.Port = port
		self.Nick = nick
		self.Password = password
		self.Chan = channel
		self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def createConnection(self):
		self.Sock.connect((self.Host, self.Port))
		self.Sock.send("NICK " + self.Nick + "\r\n")
		self.Sock.send("PASS " + self.Nick + ":" + self.Password + "\r\n")
		self.Sock.send("USER " + self.Nick + " " + self.Nick + " " + self.Nick + " :" + self.Nick + "\r\n")
 		self.Sock.send("JOIN " + self.Chan + "\r\n")

	def receiveData(self):
		return self.Sock.makefile()

	def responsePingfromServer(self, message):
		if message.startswith("PING"):
			self.Sock.send(message.replace("PING", "PONG"))

	def replyMessage(self, replies, nickname, limit):
		if len(replies) > limit:
			head = 0;
			tail = limit;
			while tail < len(replies):
				while ord(replies[tail]) & 0xc0 != 0x80:
					if tail + 1 < len(replies):
						tail = tail + 1
					else:
						break
				self.Sock.send("PRIVMSG " + self.Chan + " :"  + "%s: %s\r\n" % (nickname, replies[head:tail].replace("\n", "")))
				print ">>> " + replies[head:tail]
				time.sleep(1)
				head = tail
				tail = tail + limit
				if tail > len(replies):
					self.Sock.send("PRIVMSG " + self.Chan + " :"  + "%s: %s\r\n" % (nickname, replies[head:len(replies)].replace("\n", "")))
					print ">>> " + replies[head:len(replies)]
		else:
			for reply in replies.strip().split("\n"):
				self.Sock.send("PRIVMSG " + self.Chan + " :"  + "%s: %s\r\n" % (nickname, reply))
				print ">>> " + reply
