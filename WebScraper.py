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
csv_writer.writerow(['Sr. No', 'Product Name', 'Price', 'Website'])
#Begin an instance of the webDriver

url = 'https://www.amazon.in'
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


n=[]
p=[]
navigation = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-disabled-last')
count = 0
while count <= 3:

    for result in soup.find_all('div', {'data-component-type':'s-search-result'}):
        # print('hi')
        if result == None:
            continue
        name = result.find('span', 'a-size-medium a-color-base a-text-normal')
        price = result.find('span','a-price-whole')
        if name != None and price != None:
            n.append(name.text)
            p.append(price.text)

    if navigation != None:
        break
    nextPage = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-normal').a['href']
    url = 'https://www.amazon.in' + nextPage
    # print(url)
    url.format(soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-normal').a['href'])
    print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    navigation = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-disabled-last')

    count = count + 1

driver.quit()
system('cls')

for i in range(len(n)):
    if i >= len(p):
        break
    csv_writer.writerow([(i+1), n[i], '₹'+p[i], 'Amazon.in'])

print('Amazon Done')



