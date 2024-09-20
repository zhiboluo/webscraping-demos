import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from scrapy.http import Request
import os
import subprocess

## using selenium
import time
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


class Bt1024Spider(scrapy.Spider):
    name = "bt1024selenium"
    allowed_domains = ["1723839975-n817.xp1024-2025.cc", "b23.07pbc.cc", "ww1.07pbc.cc", "*"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519023.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7520111.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519780.html"]
    start_urls = ["https://1724786688-v828.c856q318.xyz/pw/html_data/3/2409/7539308.html"]
    # start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7527352.html"]
    # start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519162.html"]
    

    def parse(self, response):
        product_list = response.xpath('//div[@class="f14"]/text()')

        total_num = len(response.xpath('//div[@class="f14"]/img'))
        imgs = response.xpath('//div[@class="f14"]/img/@src').getall()
        # for img in imgs:
        #     image_url = response.urljoin(img)
        #     print(image_url)
        #     yield {'image_urls': [image_url]}

        torrent_links  = response.xpath('//div[@class="f14"]/a/@href').getall()
        for link in torrent_links :
            print(link)
            yield response.follow(url=link, callback=self.parse_torrent)
            # break

        # name = response.xpath('//*[@id="read_tpc"]/text()[4]').get().replace('\u3000', '').strip()

        # # Return data extracted
        # yield {
        #     'name':name,
        # }

    def save_file(self, response):
        # Save the torrent file
        # Define your folder here
        folder = 'torrent_files'
        # Ensure the folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Extract the file name from the URL
        file_name = response.url.split('/')[-1]
        
        # Add the file extension, e.g., '.torrent'
        file_name_with_extension = f"{file_name}.torrent"

        # Create the full path for saving the file
        file_path = os.path.join(folder, file_name_with_extension)
        
        # Write the file to the specified path
        with open(file_path, 'wb') as file:
            file.write(response.body)
        self.logger.info(f'File saved to {file_path}')
    
            
        # Run the torrent download script
        # For aria2
        # subprocess.run(['aria2c', file_path], check=True)
        # Or for libtorrent (if you have a script for it)
        # subprocess.run(['python', 'path/to/libtorrent_script.py'], check=True)

    # Getting data inside the "link" website
    def parse_torrent(self, response):
        # downloadlink = response.xpath('//*[@id="hash2"]/@href').get()
        # absolute_url = response.urljoin(downloadlink)
        # print(absolute_url)
        # yield Request(absolute_url, callback=self.save_file)

        # Path to the chromedriver executable
        chromedriver_path = '/Users/zhiboluo/Documents/WebScraping_python/chromedriver-mac-x64/chromedriver'

        # Set up Chrome options (if needed)
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        download_dir = '/Users/zhiboluo/Documents/WebScraping_python/webscraping-demos/scrapy/spider_tutorial/torrent_files/'  # Replace with your desired download directory path
        prefs = {
            "download.default_directory": download_dir,  # Set the download directory
            "download.prompt_for_download": False,       # Disable download prompt
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
            }
        chrome_options.add_experimental_option("prefs", prefs)

        # Set up the Service object with the path to the chromedriver executable
        service = Service(chromedriver_path)

        # Initialize the Chrome driver with the Service and Options
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Load the page
        driver.get(response.url)

        # Simulate button click
        try:
            button = driver.find_element(By.XPATH, '//*[@id="hash2"]')  # Replace with your button's XPath
            button.click()

            # Give the page some time to load the result of the click
            driver.implicitly_wait(5)  # Adjust the wait time if necessary
            time.sleep(3)
            # Get the updated page source
            # updated_page_source = driver.page_source

            # Create a Scrapy response from the updated page source
            # updated_response = HtmlResponse(driver.current_url, body=updated_page_source, encoding='utf-8')

            # Continue parsing with the updated page
            # self.parse_updated_page(updated_response)

        finally:
            driver.quit()

        # def parse_updated_page(self, response):
        # # Your code to handle the updated page goes here
        # pass