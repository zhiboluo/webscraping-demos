#Starts up our Driver and loads up our starting webpage


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Path to the chromedriver executable
chromedriver_path = '/home/ezhiblu/webscraping_python/chromedriver'

# Set up Chrome options (if needed)
chrome_options = Options()
# Example: chrome_options.add_argument("--headless")  # Uncomment if you want to run headless

# Set up the Service object with the path to the chromedriver executable
service = Service(chromedriver_path)

# Initialize the Chrome driver with the Service and Options
driver = webdriver.Chrome(service=service, options=chrome_options)



driver.get('https://www.google.com/')

#inputting text into a box
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

box.send_keys('web scraping')
box.send_keys(Keys.ENTER)


#clicking on a button
button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/a/div')
button.click()
link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div[1]/a/h3').click()
data_scraping = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]/a[1]').click()


#taking a screenshot
driver.save_screenshot('./screenshot.png')
driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div[1]/a/h3').screenshot('C:\Web Scraping course\screenshot2.png')

#full example - uses inputting text into a box, clicking on a button, and taking a screenshot
driver = webdriver.Chrome('C:/Web Scraping course/chromedriver.exe')
driver.get('https://www.google.com/')
box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img').screenshot('C:\Web Scraping course\giraffe.png')

#self scrolling
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,6000)')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


#wait times
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC
import time

box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'cntratet')))























