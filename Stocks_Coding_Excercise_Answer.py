#!/home/ezhiblu/webscraping_python/env/bin/python3



#to change to any stock just replace the url to another stocks url


# 1. Import the HTML into python
import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(response.status_code) 
print(response.text[:500])  # Print the first 500 characters of the page content

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'lxml')


# #2. get the current price of the stock
# price = soup.find('bg-quote', class_ = 'value')
# print(price)

#3. get closing price of stock 
# closing_price = soup.find('td', class_ = 'table__cell u-semi').text
# closing_price

# #4. 52 week range (lower, upper)
# nested = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')
# nested

# lower = nested.find_all('span', class_ = 'primary')[0].text
# lower

# upper = nested.find_all('span', class_ = 'primary')[1].text
# upper

# #5. analyst rating
# rating = soup.find('li', class_ = 'analyst__option active').text
# rating




