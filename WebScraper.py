# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:33:09 2021

@author: yashnagle
"""

from bs4 import BeautifulSoup
import requests
import csv
from os import system
from msedge.selenium_tools import Edge, EdgeOptions


csv_file = open('amazon_scrape.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sr. No', 'Product Name', 'Price'])
#Begin an instance of the webDriver

# url = 'https://www.amazon.in'
# driver.get(url)
# search=input('Search:\n')
search = input('Search: \n')
def get_url(search_term):
    template = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss'
    search_term=search_term.replace(' ', '+')
    return template.format(search_term)

url = get_url(search)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options= options)

driver.get(url)

#Extracting values
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()
system('cls')
n=[]
p=[]
for name in soup.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
    n.append(name.text)
for price in soup.find_all('span', class_='a-price-whole'):
    p.append(price.text)

for i in range(len(n)):
    if i >= len(p):
        break
    csv_writer.writerow([(i+1), n[i], p[i]])


