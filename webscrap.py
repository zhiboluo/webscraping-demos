#!/home/ezhiblu/webscraping_python/env/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
# import lxml
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.text, 'lxml')


#### Tag
# print(soup)
# print(soup.header)
# print(soup.div)

#### Navigable strings
# print(soup.header.p)
# print(soup.header.p.string)


#### Attributes
tag = soup.header.a
# print(tag)
# print(tag.attrs)
# print(tag.attrs['data-bs-toggle'])


## insert a new attribute
# tag['new_attribute'] = 'this is a new attribute'
# print(tag.attrs)

#### find
# print(soup.find('header'))
# print(soup.header.attrs)

# print(soup.find('div', {'class': 'container test-site'}))
# print(soup.find('h4',{'class': 'price float-end card-title pull-right'}).string)
# print(soup.find('h4',{'class':'pull-right price'}))


#### find_all   -- part 1
# print(soup.find_all('h4', {'class':'price float-end card-title pull-right'}))
# print(soup.find_all('a', class_ = 'title'))
# print(soup.find_all('p', class_ = 'review-count'))
# print(soup.find_all('h4', {'class':'price float-end card-title pull-right'})[4:])


#### find_all   -- part 2
# print(soup.find_all(['h4', 'p', 'a']))
# print(soup.find_all(id = True))
# print(soup.find_all(string = 'Iphone'))

import re
# print(soup.find_all(string = re.compile('Nok')))
# print(soup.find_all(string = ['Iphone', 'Nokia X']))
# print(soup.find_all(class_ = re.compile('pull')))
# print(soup.find_all('h4', class_ = re.compile('pull')))
# print(soup.find_all('h4', class_ = re.compile('pull'), limit = 2))


#### find_all   -- part 3
product_name = soup.find_all('a', class_ = 'title')
# print(product_name)
price = soup.find_all('h4', class_ = 'price float-end card-title pull-right')
# print(price)
reviews = soup.find_all('p', class_ = 'review-count')
# print(reviews)
description = soup.find_all('p', class_ = 'description')
# print(description)

## construct a list for each column
product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
# print(product_name_list)

price_list = []
for i in price:
    name = i.text
    price_list.append(name)
# print(price_list)

reviews_list = []
for i in reviews:
    name = i.text
    reviews_list.append(name)
# print(reviews_list)

description_list = []
for i in description:
    name = i.text
    description_list.append(name)
# print(description_list)

import pandas as pd
table = pd.DataFrame({'Product Name': product_name_list, 
                        'Description': description_list,
                        'Price': price_list,
                        'Reviews': reviews_list})
# print(table)


#### Extract data from nested html tages
boxes = soup.find_all('div', class_ = 'col-md-4 col-xl-4 col-lg-4')
# print(len(boxes))

box2 = soup.find_all('div', class_ = 'col-md-4 col-xl-4 col-lg-4')[2]
text = box2.find('a').text
print(text)
text = box2.find('p', class_ = 'description').text
print(text)
