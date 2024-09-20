import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from scrapy.http import Request
import os
import subprocess

class Bt1024Spider(scrapy.Spider):
    name = "bt1024scrapy"
    allowed_domains = ["1723839975-n817.xp1024-2025.cc", "b23.07pbc.cc", "ww1.07pbc.cc"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519023.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7520111.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519780.html"]
    # start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519162.html"]

    def parse(self, response):
        product_list = response.xpath('//div[@class="f14"]/text()')

        total_num = len(response.xpath('//div[@class="f14"]/img'))
        imgs = response.xpath('//div[@class="f14"]/img/@src').getall()
        for img in imgs:
            image_url = response.urljoin(img)
            yield {'image_urls': [image_url]}

        torrent_links  = response.xpath('//div[@class="f14"]/a/@href').getall()
        for link in torrent_links :
            print(link)
            yield response.follow(url=link, callback=self.parse_torrent)

        name = response.xpath('//*[@id="read_tpc"]/text()[4]').get().replace('\u3000', '').strip()

        # Return data extracted
        yield {
            'name':name,
        }

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
        downloadlink = response.xpath('//*[@id="hash2"]/@href').get()
        absolute_url = response.urljoin(downloadlink)
        print(absolute_url)
        yield Request(absolute_url, callback=self.save_file)