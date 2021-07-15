# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:33:09 2021

@author: yashnagle
"""

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
#print(source)
soup = BeautifulSoup(source, 'lxml')

#header = soup.find('div', class_='entry-content').text
#print(header)




count = 1

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video Link', 'Date'])
for article in soup.find_all('article'):
    print(count)
    #print(article.prettify())
    headline = article.h2.a.text
    print('Headline: ', headline)#title
    summary = article.find('div', class_='entry-content').p.text
    print('Summary: ', summary) #Summary
    date = article.find('time',class_='entry-time').text
    print('Date: ', date)#time
    ytLink = None
    try:
        vid_source = article.find('iframe', class_='youtube-player')['src']
        #print(vid_source)
    
        vid_id=vid_source.split('/')[4].split('?')[0]
        #print(vid_id)
        ytLink = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        ytLink = None
    print('Youtube Link: ', ytLink)
    count = count + 1
    
    print()
    csv_writer.writerow([headline, summary, ytLink, date])
    
csv_file.close()
    
    
#for i in range(len(l)):
#   print(t[i])
#   print(l[i])
#   print(c[i])

#   print()



