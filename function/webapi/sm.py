import urllib.request
import json

smURL = "http://xiaofengrobot.sinaapp.com/web.php?para="
def reply(string):
	try:
		response = urllib.request.urlopen(smURL + urllib.request.quote(string.encode("utf8")))
		data = response.read()
		finalResult = data[6:-2]
		return finalResult.decode("unicode-escape")
	except:
		#调用小黄鸡api
		try:
			response = urllib.request.urlopen(API + urllib.request.quote(string.encode("utf8")))
			return r.json()['response'].encode("utf-8")
		except:
			return "玩坏了Orz..."
		