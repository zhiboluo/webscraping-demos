
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to the chromedriver executable
chromedriver_path = '/home/ezhiblu/webscraping_python/chromedriver'

# Set up Chrome options (if needed)
chrome_options = Options()
# Example: chrome_options.add_argument("--headless")  # Uncomment if you want to run headless

# Set up the Service object with the path to the chromedriver executable
service = Service(chromedriver_path)

# Initialize the Chrome driver with the Service and Options
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get('https://www.nike.com/ca/w/sale-3yaep')

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#Imports the HTML of the webpage into python  
soup = BeautifulSoup(driver.page_source, 'lxml')

#grabs the HTML of each product
product_card = soup.find_all('div', class_ = 'product-card__body')

#Creates a dataframe
df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''], 'Price':[''], 'Sale Price':['']})

#Grabs the product details for every product on the page and adds each product as a row in our dataframe
for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text
        subtitle = product.find('div', class_ = 'product-card__subtitle').text
        full_price = product.find('div', class_ = 'product-price ca__styling is--striked-out css-0').text
        sale_price = product.find('div', class_ = 'product-price is--current-price css-1ydfahe').text
        df.loc[len(df)] = {'Link':link, 'Name':name, 'Subtitle':subtitle, 'Price':full_price, 'Sale Price':sale_price}
    except:
        pass

#exports the dataframe as a csv
df.to_csv('infinite_scrolling_nike.csv')



