#!/usr/bin/env python
# -*-coding:utf-8-*- 
import urllib2,urllib,json
url="http://new.club.weibo.com/dida/interface/team/audit"
#response=urllib2.urlopen("http://www.google.com")
#url2=response.geturl()
#print url2
date={'status':4}
team_id=raw_input("请输入要下线的项目ID:")
if isinstance(team_id,int):
	date["pid"]=team_id
else:
	print "输入错误"
#date={
		#'pid':'380',
		#'status':'4',
		#}
REQ=urllib2.urlopen(url,urllib.urlencode(date)).read()
tt=json.loads(REQ)
print tt["errmsg"]
