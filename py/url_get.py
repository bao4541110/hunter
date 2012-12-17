#!/usr/bin/env python
# -*-coding:utf-8-*- 
import urllib2,urllib,json,random
uids=[]
i=0
for i in range(0,20):
		test_date=random.randint(
		0000000001,9999999999)
		uids.append(str(test_date))
		i+=1
print uids
dd=','.join(uids)
print dd
url="http://dida1.club.weibo.com/dida/interface/coupon/getnumber"
#response=urllib2.urlopen("http://www.google.com")
#url2=response.geturl()
#print url2
date={}
team_id=raw_input("请输入User_ID:(不输入将默认使用上面的随机数）")
if team_id: 
	date["uids"]=team_id
else:
	date["uids"]=dd
print date
param=urllib.urlencode(date)
print param
REQ=urllib2.urlopen("%s?%s"%(url,param)).read()
try:
	tt=json.loads(REQ)

	print tt["msg"]
except:
	
	print REQ
