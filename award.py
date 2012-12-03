#! usr/bin/env python
# coding=utf-8
import time,random
file=open("/home/hunter/workspace/list.txt")
tt=file.readlines()
jj=[]
#print tt
#print type(tt)
key=raw_input("请输入要抽取的奖项(数字) ")
if key !="1":
	val=input("情输入要抽取的个数")
	if isinstance(val,int):
		val1=0-val
	else:
		print "请重新输入要抽取的个数:"
		val =input()
		val1=0-int(val)
	
else:pass	
a=time.time();x=1
try:
	while 1:
		for i in tt:
			jj.append(i)
			print i.decode('utf-8')
except KeyboardInterrupt:
	print "time is up"
if key == "1":
	print "一等奖中奖者是",i
elif key !="1":
	jj1=random.sample(tt,val)
	#jj1=jj[val1: ] 
	print key+"等奖， 抽取"+str(val)+"人，中奖者是："
	for i in jj1:
		print i,
x=time.time()
print x-a
