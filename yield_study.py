#! usr/bin/env python
# coding=utf-8
def fab():
	a=b=1
	yield a
	yield b
	while 1:
		a,b=b,a+b
		yield b
for num in fab():
	if num >5000: break
	print num,
