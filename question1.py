'''libraries to be installed for using this script:
*   bs4
*   requests
*   newspaper3k
*   nltk
*   time
*   pandas
#Installing Library'''
!pip3 install newspaper3k

#importing Libraries
from bs4 import BeautifulSoup
import requests
from newspaper import Article
import nltk
import time
nltk.download('punkt')
import pandas as pd

#Search function
def keywords_search(article):
  article=article.replace('\n',' ')
  for lines in nltk.tokenize.sent_tokenize(article):
    if 'surge' in lines or  'acquisitions' in lines or 'IPO' in lines or 'initial public offering' in lines :
      print(lines)


#fetching html of page 
webdata=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
htmldata=webdata.text
soup=BeautifulSoup(htmldata,'lxml')

#declaring list variables
news_title=[]
news_link=[]
news_summary=[]
news_date=[]
subnews_title=[]
subnews_link=[]
subnews_summary=[]
subnews_date=[]

a = soup.find("div", attrs={'class':'fe4pJf'})    #finding a div tag with mentioned class
list=a.find_all("div", attrs={'class':'NiLAwe'}) #finding all div tag with mentioned class

for i in list:
  k=0 #used to identify if it is a main news or subnews
   for j in i.find_all('a',attrs={'class':'DY5T1d'}):      #finding a tag with mentioned class
    url="https://news.google.com"+j['href'][1:]           #gets all the url of the article on that page
    if(requests.get(url).status_code==200):       #checking if url is correct or not
      
      article = Article("https://news.google.com"+j['href'][1:], language="en")
      article.download()
      article.parse() 
      article.nlp()

      title=j.title #Use same title as google news 
      summary=article.summary
      date=article.publish_date

      print("Title: "+title+"\nSearching keywords:")  #printing lines containing keywords.
      keywords_search(article.text)
      
      if(k==0):   #main news index
        news_title.append(title)
        news_summary.append(summary)
        news_url.append(url)
        news_date.append(date)
      else:       #subnews 
        subnews_title.append(title)
        subnews_summary.append(summary)
        subnews_url.append(url)
        subnews_date.append(date)
      k+=1    
      time.sleep(3)      

#making tables using panda
news_table=pd.DataFrame({'Main news title':news_title,'Summary':news_summary,'URL':news_url,'Date and Time':news_date})
subnews_table=pd.DataFrame({'Sub news title':subnews_title,'Summary':subnews_summary,'URL':subnews_url,'Date and Time':subnews_date})

print("Head of News table")
news_table.head()
print("Head of Sub News table")
subnews_table.head()
