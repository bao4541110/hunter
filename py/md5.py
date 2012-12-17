#!/usr/bin/env python
# -*-coding:utf-8-*-
'''check file or string md5 value, you can type file/str after this file'''
import sys 
import hashlib
try:
	test=sys.argv[1]
except:
	test=raw_input("请输入完整路径的文件名或者字符：")
try:
	file=open(test,'r')
	checkmd5=hashlib.md5()
	checkmd5.update(file.read())
	getfile_md5=checkmd5.hexdigest()
	print "%s 文件的md5值是:" %test
except:
	print "%s的md5值" %	test
	getfile_md5=hashlib.md5(test).hexdigest().upper()


print getfile_md5

