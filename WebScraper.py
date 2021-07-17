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

valDict={}
csv_file = open('amazon_flipkart_scrape.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sr. No', 'Product Name', 'Price(Rs)', 'Link' ,'Website'])
#Begin an instance of the webDriver

url = 'https://www.amazon.in'
# driver.get(url)
# search=input('Search:\n')
search = input('Search: \n')
def get_url(search_term, aa):
    if aa == 'amazon':
        template = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss'
        search_term=search_term.replace(' ', '+')
        return template.format(search_term)
    elif aa == 'flipkart':
        template = 'https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        search_term = search_term.replace(' ', '%20')
        return template.format(search_term)
url = get_url(search, 'amazon')
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options= options)
driver.get(url)

# Extracting values
soup = BeautifulSoup(driver.page_source, 'lxml')
ab = 'a-size-medium a-color-base a-text-normal'
ba = 'a-size-base-plus a-color-base a-text-normal'
n=[]
p=[]
l = []
navigation = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-disabled-last')
count = 0
while count <= 3:

    for result in soup.find_all('div', {'data-component-type':'s-search-result'}):
        if result == None:
            continue
        name = result.find('span', class_=ab)
        if name == None:
            name = result.find('span', class_=ba)
        price = result.find('span','a-price-whole')
        list1 = 'https://www.amazon.in/result.find'+result.find('a', class_='a-link-normal a-text-normal')['href']
        system('cls')
        print('name: ',name)
        print('price: ', price)
        print(list1)
        if name != None:
            n.append(name.text)
        else:
            n.append('None')
        
        if price !=None:
            p.append(price.text)
        else:
            p.append('0')
        if list1 != None:
            l.append(list1)
        else:
            l.append('None')
        

    if navigation != None:
        break
    nextPage = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-normal').a['href']
    url = 'https://www.amazon.in' + nextPage
    # print(url)
    url.format(soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-normal').a['href'])
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    navigation = soup.find('div', class_='a-section a-spacing-none a-padding-base').find('li',class_='a-disabled-last')


    count = count + 1

# driver.quit()
# system('cls')
i = 0
for i in range(len(n)):
    if i >= len(p):
        break
    pr = p[i].replace(',','')
    if int(pr) in valDict:
        valDict[int(pr)].append([0, n[i], p[i], l[i], 'Amazon.in'])
    else:
        valDict[int(pr)] = []
        valDict[int(pr)].append([0, n[i], p[i], l[i], 'Amazon.in'])

print('Amazon Done')

url1=get_url(search,'flipkart')
n1=[]
p1=[]
l1=[]
driver.get(url1)
soup = BeautifulSoup(driver.page_source, 'lxml')
# s = soup.find('a', class_='_1fQZEK')
system('cls')
# print(s)
# s = soup.find('div', class_='_2MImiq')
# print(s.find('a', class_='ge-49M')['href'])
ab = '_1fQZEK'
ba = 's1Q9rs'
if soup.find('a', class_=ab) == None:
    ab = ba
for re in soup.find_all('a', class_=ab):
    if re == None:
        continue
    name = re.find('div', class_='_4rR01T')
    if name == None:
        name=re.find('div', class_='s1Q9rs')
    if name == None:
        n.append(re.text)
    else:
        n1.append(name.text)
    # print(re.find('div', class_='_4rR01T').text)
    price = re.find('div', class_='_30jeq3 _1_WHN1')
    if price == None:
        price=re.find('div', class_='_30jeq3')
    if price == None:
        p1.append('₹0')
    else:
        
        p1.append(price.text)
    # print(re.find('div', class_='_30jeq3 _1_WHN1').text)
    l1.append('https://www.flipkart.com/'+re['href'])


# sys.exit()

for j in range(len(n1)):
    if j >= len(p1):
        break
    pr = p1[j][1:].replace(',','')

    if int(int(pr)) in valDict:
        valDict[int(pr)].append([0, n1[j], p1[j][1:], l1[j],'Flipkart'])
    else:
        valDict[int(pr)] = []
        valDict[int(pr)].append([0, n1[j], p1[j][1:], l1[j] ,'Flipkart'])

key = list(valDict.keys())
key.sort(reverse=True)

ij = 1
for k in key:
    for arr in valDict[k]:
        arr[0] = ij
        csv_writer.writerow(arr)
        ij = ij + 1
csv_file.close()

driver.quit()
system('cls')
print('DONE')