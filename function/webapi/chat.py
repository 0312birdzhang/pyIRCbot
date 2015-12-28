import urllib.request
import json

chatURL = "http://www.tuling123.com/openapi/api?key=b1833040534a6bfd761215154069ea58&info="
API="http://sandbox.api.simsimi.com/request.p?key=0eca389b-d21a-46d3-9606-826176396c44&lc=zh&ft=1.0&text="
def reply(string):
	#调用小黄鸡api
	try:
		response = urllib.request.urlopen(API + urllib.request.quote(string.encode("utf8")))
		return r.json()['response'].encode("utf-8")
	except:
		return "玩坏了Orz..."
