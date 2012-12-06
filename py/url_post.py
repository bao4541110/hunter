import urllib2,urllib,json
url="http://new.club.weibo.com/dida/interface/team/audit"
#response=urllib2.urlopen("http://www.google.com")
#url2=response.geturl()
#print url2
date={
		'pid':'399',
		'status':'4',
		}
REQ=urllib2.urlopen(url,urllib.urlencode(date)).read()
tt=json.loads(REQ)
print tt["errmsg"]
