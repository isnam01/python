#!usr/bin/python
import os
import crypt
str=input("Enter the username")
b=str.isalpha()
if b :
 print("user can be created")
 pw="hello"+str
 passwd=crypt.crypt(pw,"*")
 os.system("useradd -p "+passwd+" "+str)

else :
 print("User cannot be created")
	
	 

