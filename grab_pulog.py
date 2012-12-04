#!usr/bin/env python 
#coding=utf-8
import urllib2,re,time,threading
Base_url="http://www.pulog.org"
Req=urllib2.urlopen(Base_url)
print Req.read()
