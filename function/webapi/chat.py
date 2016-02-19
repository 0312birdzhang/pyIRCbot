#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

API="http://127.0.0.1:10088/openxiaoice/ask?q="

def reply(string):
	try:
		req = urllib.request.Request(API + urllib.request.quote(string.encode("utf8")))
		req = urllib.request.urlopen(req).read()
		ans = json.loads(req.decode('utf-8'))["answer"]
		print(ans)
		return ans
	except Exception as e:
		print(e)
		return "玩坏掉了Orz..."

if __name__ == "__main__":
	reply("Hello")