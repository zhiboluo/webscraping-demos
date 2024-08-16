import requests

from bs4 import BeautifulSoup

import pandas as pd

  

#Imports the HTML into python

page = requests.get('https://www.carpages.ca/used-cars/search/?num_results=50&fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7&p=1')

soup = BeautifulSoup(page.text, 'lxml')

# soup

  

#Creating our dataframe

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Price':[''], 'Color':['']})

# pd.__version__ 

counter = 0

#This loop goes through the first 10 pages and grabs all the details of each posting

while counter < 10:

    #gets the HTML of all the postings on the page

    postings = soup.find_all('div', class_ = 't-flex t-gap-6 t-items-start t-p-6')

  

    #grabs all the details for each posting and adds it as a row to the dataframe

    for post in postings:

        link = post.find('a', class_ = 't-flex t-items-start t-w-[130px] t-shrink-0').get('href')

        # print(link)

        link_full = 'https://www.carpages.ca' +link

        name = post.find('h4', class_ = 'hN').text.strip()

        try:
            price = post.find('span', class_ = 't-font-bold t-text-xl' ).text
        except:
            price = post.find('span', class_ = 't-font-bold t-text-xl t-text-primary' ).text 
        
        
        color = post.find_all('span', class_ = 't-text-sm t-font-bold')[0].text.strip()
        
        #df = df.append({'Link':link_full, 'Name':name, 'Price':price, 'Color':color}, ignore_index = True)
        df.loc[len(df)] = {'Link':link_full, 'Name':name, 'Price':price, 'Color':color}
    
    
    #grabs the url of the next page

    next_page = soup.find('a', class_ = 'nextprev').get('href')

    #Imports the next pages HTML into python

    page = requests.get('https://www.carpages.ca' + next_page)

    soup = BeautifulSoup(page.text, 'lxml')

    counter += 1

  

df.to_csv('./scraped_table_car.csv')
print(df)