#! usr/bin/env python
# coding=utf-8
import urllib,urllib2,json,re

x=raw_input('请输入ip地址:')
base_url='http://ip.taobao.com/service/getIpInfo.php'
get_data={'ip':x
		}
get_data=urllib.urlencode(get_data)
#print get_data
data=urllib2.urlopen(base_url+'?'+get_data).read()
test=json.loads(data)
#print type(test)
if test["code"]==0:
	print "获取成功IP:",test["data"]["ip"]
	print "信息",test["data"]["country"],test["data"]["region"],test["data"]["city"],test["data"]["area"]
else:
	print "获取IP信息失败"
for i in test["data"]:
	print type(i)
	print i.values
