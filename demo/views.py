from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import webbrowser
import re

driver = webdriver.Chrome(executable_path=r'C:\Users\Yogesh\Downloads\chromedriver.exe')
driver.get("https://techcrunch.com/")

def data_scrapping(request):
    news_titles=[] 
    times=[] 
    Images= []
    authors= []
    
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    for a in soup.findAll('article', attrs={'class':'post-block post-block--image post-block--unread'}):
        news_title=a.find('h2', attrs={'class':'post-block__title'})
        author=a.find('span', attrs={'class':'river-byline__authors'})
        time=a.find('time', attrs={'class':'river-byline__full-date-time'})
        #image=a.find('figure', attrs={'class':'post-block__media'})
        

        news_titles.append(news_title.text)
        authors.append(author.text)
        times.append(time.text)
        print(times)
        #images.append(image.txt) 
    
    images = soup.find_all('img', {'src':re.compile('.jpg')})
    for image in images: 
        print(image['src']+'\n')
      
        
        
    df = pd.DataFrame({'NEWS_TITLE':news_titles,'AUTHOR':authors,'TIMESTAM':times,})
    df.to_csv('product_demo3.csv', encoding='utf-8')   
    data = pd.read_csv(r'C:\Users\Yogesh\Desktop\Project_collection\data_scrapping\scrapping\product_demo3.csv')
    html = data.to_html()
    path = os.path.abspath('data_demo1.html')
    url = 'file://' + path

    with open(path, 'w', encoding="utf-8") as f:
        f.write(html)
    return webbrowser.open(url)