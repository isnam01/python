!pip install stockstats

#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import stockstats as ss
import time

#Declaring variables
company=[]
lastprice=[]
pcmax=[]
pcmin=[]
maxtime=[]
mintime=[]

#alert function
def alert(c,i):         #a function that alerts for a change 
  if(c):
    str="the stock price of company {} showed an {} percentage increase in value in last {} seconds".format(company[i],pcmax[i]-pcmin[i],maxtime[i]-mintime[i])
    print(str)
  else:
    str="the stock price of company {} showed an {} percentage decrease in value in last {} seconds".format(company[i],pcmax[i]-pcmin[i],mintime[i]-maxtime[i])
    print(str)

webdata=requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
curtime=time.time() #gets the current time in datetime format
htmldata=webdata.text #get the data on the webpage

soup=BeautifulSoup(htmldata,'lxml') #converts the data into html format
a = soup.find("table", attrs={'class':'tbldata14 bdrtpg'})    #finds the table with the mentioned class on the webpage

for tr in a.find_all('tr')[1:]:
    td=tr.find_all('td')
    company.append(td[0].find('b').text)
    lastprice.append(float(td[2].text.replace(',','')))
    pcmin.append(float(td[4].text))
    pcmax.append(float(td[4].text))
    maxtime.append(curtime)
    mintime.append(curtime)

time.sleep(30)

# run the funtion for specific time period
t_end = time.time() + 60*10  #converting minutes into seconds 
while time.time() < t_end:
  
  curtime=time.time()
  i=0

  webdata=requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")  #gets the webdata
  htmldata=webdata.text
  soup=BeautifulSoup(htmldata,'lxml')
    
  a = soup.find("table", attrs={'class':'tbldata14 bdrtpg'})
  
  for tr in a.find_all('tr')[1:]:   #finds all the tr tag in a
    td=tr.find_all('td')
    cur=float(td[4].text)     #type conversion 
    
    if(cur>=pcmax[i]):     
      maxtime[i]=curtime
      pcmax[i]=cur
      if(pcmax[i]-pcmin[i]>=2): #comparing the difference in the value
        alert(1,i)        #calling the function alert
    
    else:
      if(cur<=pcmax[i]):
        mintime[i]=curtime
        pcmin[i]=cur
        if(pcmax[i]-pcmin[i]>=2):
          alert(0,i)
    i+=1
  
  time.sleep(30)
