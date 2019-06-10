#!/usr/bin/python
import datetime 
str=input("enter your name")
time =datetime.datetime.now().hour
if time>=21 and time<4 :
	print("GOOD NIGHT ",str)
elif time>=4 and time<12 :
	print("GOOD MORNING ",str)
elif time>=12 and time<17 :
	print("GOOD AFTERNOON ",str)
elif time>=17 and time<21 :
	print("GOOD NIGHT ",str)

