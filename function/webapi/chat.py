import urllib.request
import json

API="http://127.0.0.1:10058/openxiaoice/ask?q="
def reply(string):
	#调用小黄鸡api
	try:
		response = urllib.request.urlopen(API + urllib.request.quote(string.encode("utf8")))
		return r.json()['answer'].encode("utf-8")
	except:
		return "玩坏掉了Orz..."
