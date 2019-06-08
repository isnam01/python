#!usr/bin/python
from googlesearch import search
import webbrowser
str=input("enter the search element")
x=search(str, tld='com', lang='en', num=5, start=0, stop=5, pause=2.0)
webbrowser.open_new_tab("http://www.google.com/search?q="+str)
for i in x :
    print (i)
    webbrowser.open_new_tab(i)
