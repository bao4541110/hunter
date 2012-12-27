#!/usr/bin/env python
# -*-coding:utf-8-*-
import re
text = 'hi,boys and \girls'
no = '15610531170'
Reg=re.compile(r"^1[3,8,5]+?\d{9}")
print re.split('\s',text)
print re.findall(r"\\girls",text)
print Reg.findall(no)
def mul(x):
	return x**2
test=[1,2,3,4,5,6,7,8,9,10]
print map(mul,test)
