#!usr/bin/python
import os
cmnd=input()
a=os.system(cmnd +" 2>/dev/null")
if a :
	print("command doesnot exist")
else :
	print("command exist")
