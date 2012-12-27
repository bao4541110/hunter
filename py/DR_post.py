#!/usr/bin/env python
# -*-coding:utf-8-*- 
import urllib2,urllib,json
dd=raw_input("请输入要驳回的类型，1：项目 其他为广告")
info='''2 对应通过 3 对应驳回 4 对应失败'''
team_url="http://dida.club.weibo.com/dida/interface/team/audit"
ad_url="http://dida.club.weibo.com/dida/interface/ad/audit"

date={}
team_id=raw_input("请输入ID:")
if dd==1: 
	date["pid"]=team_id
	url=team_url
else:
	
	date["pid"]=team_id
	url=ad_url
print info
status=raw_input("输入参数2/3/4：")
refuse=raw_input("输入理由:")
date["status"]=status
date["refuse"]=refuse
#date={
		#'pid':'380',
		#'status':'4',
		#}
REQ=urllib2.urlopen(url,urllib.urlencode(date)).read()
print REQ
tt=json.loads(REQ)
print tt["errmsg"]
