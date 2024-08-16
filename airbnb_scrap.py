#!/home/ezhiblu/webscraping_python/env/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

#Imports the HTML into python
url = 'https://www.airbnb.ca/s/Central-America/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-09-01&monthly_length=3&monthly_end_date=2024-12-01&price_filter_input_type=0&channel=EXPLORE&search_type=filter_change&price_filter_num_nights=5&place_id=ChIJEQho98BYC48RcCULBsfgrI0&date_picker_type=calendar&checkin=2024-08-21&checkout=2024-08-23&source=structured_search_input_header'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
page = requests.get(url, headers=headers)
# page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
print(soup)


# try:
#     next_page = soup.find_all('a', {'aria-label': 'Next'})[0].get('href')
# except:
# next_page = soup.find('a', {'aria-label':'Next'})
next_page = soup.find('a', class_ = 'nextprev').get('href')


next_page_full = 'https://www.airbnb.ca' + next_page
# print(next_page_full)
