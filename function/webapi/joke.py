import urllib.request
import json

doubiUrl = "http://api.xiaodoubi.com/api.php?key=73C89DC7-25EC-A32C-B6E9-2AB8BCF75249&chat="
def reply(string):
	if not string:
		return "你还没说呢"
	try:
		response = urllib.request.urlopen(jokeURL + urllib.request.quote(string.encode("utf8")))
		data = response.read()
		return data
	except:
		return "玩坏掉了。"
		