#!/usr/bin/python
from googlesearch import search
import pyqrcode
import webbrowser
a=0
s=input("enter your search")
l=search(s,tld='com',lang='en',num=3,start=0,stop=3,pause=1) 
for i in l:
    webbrowser.open_new_tab(i)
    q=pyqrcode.create(i)
    print(i)
    q.png("qr{}.png".format(a),scale=5)
    a=a+1
    

