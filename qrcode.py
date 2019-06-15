#!/usr/bin/python
from googlesearch import search
import pyqrcode
import os
a=0
s=input("enter your search")
l=search(s,tld='com',lang='en',num=3,start=0,stop=3,pause=1) 
for i in l:
    q=pyqrcode.create(i)
    print(i)
    q.png("qr{}.png".format(a),scale=5)
    os.system(" scp -i /home/mansi/Desktop/redhataws.pem qr"+str(a)+".png ec2-user@13.235.78.21:/var/www/html/")
    a=a+1
