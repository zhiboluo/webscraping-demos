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
    name = "bt1024"
    allowed_domains = ["1723839975-n817.xp1024-2025.cc", "b23.07pbc.cc", "ww1.07pbc.cc", "*"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519023.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7520111.html"]
    start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519780.html"]
    start_urls = ["https://1724786688-v828.c856q318.xyz/pw/html_data/3/2409/7539308.html"]
    # start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7527352.html"]
    # start_urls = ["https://1723839975-n817.xp1024-2025.cc/pw/html_data/3/2408/7519162.html"]
    

    def parse(self, response):
        # Extract the raw HTML content including newlines
        raw_html = response.xpath("//div[@id='read_tpc']").get()

        # Replace <br> tags with newlines
        raw_content = raw_html.replace('<br>', '\n').replace('</br>', '\n').replace('</div>', '\n')
        print("raw_content\n", raw_content)
        # Split the content using the delimiter (with preserved \n)
        split_content = raw_content.split('====================================================================================================')

        # Split the content using the delimiter
        # print("length of split_content: ", len(split_content))
        # print("split_content \n", split_content)

        i=0
        for section in split_content:
            # Clean up the data (e.g., removing unwanted newlines and spaces)
            cleaned_section = section.strip()
            if cleaned_section and self.extract_image_link(cleaned_section):
                # print(f"#######section-{i}################\n")
                i = i+1
                # print("cleaned_section \n", cleaned_section)
                # Now extract specific pieces of data from each cleaned section
                item = {
                    'title': self.extract_between(cleaned_section, "【HD/MP4】【中文字幕】", "\n"),
                    'video_code': self.extract_between(cleaned_section, "【影片名称代号】：", "\n"),
                    'format': self.extract_between(cleaned_section, "【影片格式】：", "\n"),
                    'subtitle_language': self.extract_between(cleaned_section, "【字幕语言】：", "\n"),
                    'size': self.extract_between(cleaned_section, "【影片大小】：", "\n"),
                    'hash': self.extract_between(cleaned_section, "【试证全码】：", "\n"),
                    'image_link': self.extract_image_link(cleaned_section),
                    'torrent_name': self.extract_between(cleaned_section, "【种子名称】:", "\n"),
                    'download_link': self.extract_download_link(cleaned_section),
                }
                yield item

    
    def extract_between(self, text, start, end):
        """Helper method to extract text between two markers."""
        try:
            return text.split(start)[1].split(end)[0].strip()
        except IndexError:
            return None

    def extract_image_link(self, text):
        """Helper method to extract the image link."""
        try:
            return text.split('src="')[1].split('"')[0]
        except IndexError:
            return None

    def extract_download_link(self, text):
        """Helper method to extract the download link."""
        try:
            return text.split('href="')[1].split('"')[0]
        except IndexError:
            return None
