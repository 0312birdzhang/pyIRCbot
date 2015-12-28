import urllib.request
import json

#smURL = "http://xiaofengrobot.sinaapp.com/web.php?para="
smURL = "http://www.tuling123.com/openapi/api?key=b1833040534a6bfd761215154069ea58&info="
def reply(string):
	try:
		response = urllib.request.urlopen(smURL + urllib.request.quote(string.encode("utf8")))
		data = response.read()
		result = json.loads(data.decode("utf8"))
		finalResult = result['text']
		#finalResult = data[6:-2]
		return finalResult
	except:
		return "玩坏掉了。"