from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By


# Path to the chromedriver executable
chromedriver_path = '/Users/zhiboluo/Documents/WebScraping_python/chromedriver-mac-x64/chromedriver'

# Set up Chrome options (if needed)
chrome_options = Options()
# Example: chrome_options.add_argument("--headless")  # Uncomment if you want to run headless

# Set up the Service object with the path to the chromedriver executable
service = Service(chromedriver_path)

# Initialize the Chrome driver with the Service and Options
driver = webdriver.Chrome(service=service, options=chrome_options)

web = "https://www.audible.com/search"

driver.get(web)
driver.maximize_window()



# Locating the box that contains all the audiobooks listed in the page
container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')

# Getting all the audiobooks listed (the "/" gives immediate child nodes)
products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')
# products = container.find_elements_by_xpath('./li')

# Initializing storage
book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)  # Storing data in list
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
