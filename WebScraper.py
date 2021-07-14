# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:33:09 2021

@author: yashnagle
"""

from bs4 import BeautifulSoup
import requests
import csv

searchQuery = input('What would you like to search?\n')
sq = 'https://www.amazon.in/s?k='
for w in searchQuery:
    if w == ' ':
        sq = sq + '+'
    else:
        sq = sq + w
sq = sq + '&ref=nb_sb_noss_2'

source = requests.get(sq).text
soup = BeautifulSoup(source, 'lxml')
count = 1

print(sq)
# for sp in soup.find_all('a', class_='a-link-normal a-text-normal'):
#     print(sp)
#     # print('hi')
#     # print(count)
#     # print(sp.span.text)
#     if count == 3:
#         break
#     count = count + 1

print(soup.find('a', class_='a-link-normal a-text-normal'))

