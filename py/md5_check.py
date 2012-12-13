#!/usr/bin/env python
import hashlib
test=raw_input("input a string:")
print (hashlib.md5(test).hexdigest().upper())

