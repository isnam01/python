!pip3 install newspaper3k

import urllib.request
from bs4 import BeautifulSoup
from newspaper import Article
import csv
import nltk
import time
import pandas as pd
from datetime import datetime
nltk.download('punkt')

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"

news_title=[]
news_time=[]
news_summary=[]
news_url=[]

subnews_title=[]
subnews_time=[]
subnews_summary=[]
subnews_url=[]

# Open the URL as Browser, not as python urllib
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
infile=urllib.request.urlopen(page).read()
soup = BeautifulSoup(infile,'lxml'))
section = soup.find_all("div", {"class": "xrnccd F6Welf R7GTQ keNKEd j7vNaf"})    #finding all div class with mentioned class

for a in section:
    b=a.find('a',href=True)
    toi_article = "https://news.google.com"+b['href'] # en for English
    article=Article(str(toi_article))
    article.download() #preprocessinf the news
    article.parse()  
    article.nlp() 
    #splitting the text on the basis of '.'
    for lines in article.text.split('.'): 
          if 'surge' in lines or 'IPO' in lines or 'aquisitions' in lines or 'initial public offering' in lines:     #Searching the words
            print(lines) #printing the lines having searched text
    #appending title of article
    news_title.append(article.title)    
    news_summary.append(article.summary)
    news_time.append(article.publish_date)
    news_url.append(article.url) 
    #finding one div tag with class as SbNwzf
    j=a.find("div",{"class":"SbNwzf"})    

    #finding all a tag with the mentioned class    
    for k in j.find_all("a",{"class":"VDXfz"}):       
        toi_subarticle = "https://news.google.com"+k['href'] # en for English 
        subarticle=Article(str(toi_subarticle))
        #preprocessing the news
        subarticle.download() 
        subarticle.parse()   
        subarticle.nlp() 
        for lines in subarticle.text.split('.'):
          if 'surge' in lines or 'IPO' in lines or 'aquisitions' in lines or 'initial public offering' in lines:
            print(lines)
        subnews_title.append(subarticle.title) 
        subnews_summary.append(subarticle.summary)
        subnews_time.append(str(subarticle.publish_date))
        subnews_url.append(subarticle.url)
    time.sleep(1)

#creating dictionary
news_data = {'Title':news_title,            
        'Summary':news_summary,
        'Time':news_time,
        'URL':news_url}

#coverting the dictionary to pandas dataframe        
News_table = pd.DataFrame(news_data)

subnews_data = {'Title':subnews_title,
        'Summary':subnews_summary,
        'Time':subnews_time,
        'URL':news_url}
Subnews_table = pd.DataFrame(subnews_data)

#printing head of the table
print("Head of News table")
News_table.head()

print("Head of Subnews table")
Subnews_table.head()
