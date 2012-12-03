import urllib2
response=urllib2.urlopen("http://www.google.com")
url2=response.geturl()
print url2
