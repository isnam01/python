#!/usr/bin/python
import datetime
import pip
import pyttsx3
def no_of_modules():
    a=0
    for i in pip.get_installed_distributions(local_only=True):
        a+=1
    return(a)

def sorts(l):
    l.sort()
    return (l)

def sum(x,y):
    c=x+y
    return (c)

def greet():
    time =datetime.datetime.now().hour
    s=pyttsx3.init()
    if time>=21 and time<4 :
        s.say("good night")
        s.runAndWait()   
    elif time>=4 and time<12 :
        s.say("good morning")
        s.runAndWait()
    elif time>=12 and time<17 :
        s.say("good afternoon")
        s.runAndWait()
    elif time>=17 and time<21 :
        s.say("good evening")
        s.runAndWait()

def say_name():
    st=input("enter your name")
    s=pyttsx3.init()
    s.say(st)
    s.runAndWait()

