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
count = 0

for sp in soup.find_all('span'):
    if count == 2:
        break
    print(sp)
    count = count + 1

