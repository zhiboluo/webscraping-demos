from bs4 import BeautifulSoup
import re

# Sample HTML content
html_content = """
<div class="f14" id="read_tpc">
    ====================================================================================================<br>【HD/MP4】【中文字幕】ABP973密著檔案
    FILE.05 愛音麻里亞<br>【影片名称代号】：密著檔案 FILE.05 愛音麻里亞<br>【影片格式】：MP4<br>【字幕语言】：有<br>【是否有码】：有<br>【影片大小】：1.09
    GB<br>【试证全码】：fe84db85274cc111d7cc1e432ffa049fb53e0df3<br>【作品种类期限】：7天（迅雷正式版已被官网屏蔽请下载迅雷极速版或其他下载软件）<br><img
        src="https://b23.07pbc.cc/i/2024/08/27/8fkgfgg.jpg" border="0"
        onclick="if(this.width>=1024) window.open('https://b23.07pbc.cc/i/2024/08/27/8fkgfgg.jpg');"
        onload="if(this.width>'1024')this.width='1024';"><br><br><br>(迅雷正式版已被官网屏蔽
    请下载迅雷极速版或者其他下载软件)<br><br>【种子名称】:ABP973C.torrent<br>【下载网址】: <a
        href="https://ww1.07pbc.cc/link.aspx?hash=FE84DB85274CC111D7CC1E432FFA049FB53E0DF3"
        target="_blank">https://ww1.07pbc.cc/link.aspx?hash=FE84DB85274CC111D7CC1E432FFA049FB53E0DF3</a><br><br>====================================================================================================<br>【HD/MP4】【中文字幕】BBAN283人的挑語蕾絲邊
    藍色奈木 通野未帆<br>【影片名称代号】：藍色奈木 通野未帆<br>【影片格式】：MP4<br>【字幕语言】：有<br>【是否有码】：有<br>【影片大小】：1.30
    GB<br>【试证全码】：97864f069305af89e963128a4ed3462948e1b7c6<br>【作品种类期限】：7天（迅雷正式版已被官网屏蔽请下载迅雷极速版或其他下载软件）<br><img
        src="https://b23.07pbc.cc/i/2024/08/27/ucukjr.jpg" border="0"
        onclick="if(this.width>=1024) window.open('https://b23.07pbc.cc/i/2024/08/27/ucukjr.jpg');"
        onload="if(this.width>'1024')this.width='1024';"><br><br><br>(迅雷正式版已被官网屏蔽
    请下载迅雷极速版或者其他下载软件)<br><br>【种子名称】:BBAN283C.torrent<br>【下载网址】: <a
        href="https://ww1.07pbc.cc/link.aspx?hash=97864F069305AF89E963128A4ED3462948E1B7C6"
        target="_blank">https://ww1.07pbc.cc/link.aspx?hash=97864F069305AF89E963128A4ED3462948E1B7C6</a><br><br>====================================================================================================<br>【HD/MP4】【中文字幕】CJOD245教師逆
    校外出 春咲涼<br>【影片名称代号】：教師逆 校外教學時出
    春咲涼<br>【影片格式】：MP4<br>【字幕语言】：有<br>【是否有码】：有<br>【影片大小】：1.10
    GB<br>【试证全码】：fb66efd7d5f99b93de319a800754fbe4179349fb<br>【作品种类期限】：7天（迅雷正式版已被官网屏蔽请下载迅雷极速版或其他下载软件）<br><img
        src="https://b23.07pbc.cc/i/2024/08/27/ucuqv8.jpg" border="0"
        onclick="if(this.width>=1024) window.open('https://b23.07pbc.cc/i/2024/08/27/ucuqv8.jpg');"
        onload="if(this.width>'1024')this.width='1024';"><br><br><br>(迅雷正式版已被官网屏蔽
    请下载迅雷极速版或者其他下载软件)<br><br>【种子名称】:CJOD245C.torrent<br>【下载网址】: <a
        href="https://ww1.07pbc.cc/link.aspx?hash=FB66EFD7D5F99B93DE319A800754FBE4179349FB"
        target="_blank">https://ww1.07pbc.cc/link.aspx?hash=FB66EFD7D5F99B93DE319A800754FBE4179349FB</a><br><br>
        ====================================================================================================<br><br><br>

</div>
"""

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the text from the HTML
# text = soup.get_text(separator="\n")
text = soup.get_text()
# print("text: ", text)
# Define the pattern for extracting information
pattern = re.compile(
    r'【HD/MP4】【中文字幕】(?P<title>.*?)'
    r'【影片名称代号】：(?P<name>.*?)'
    r'【影片格式】：(?P<format>.*?)'
    r'【字幕语言】：(?P<subtitle>.*?)'
    r'【是否有码】：(?P<code>.*?)'
    r'【影片大小】：(?P<size>.*?) GB'
    r'【试证全码】：(?P<hash>.*?)'
    r'【作品种类期限】：(?P<deadline>.*?)'
    # r'<img\s+src="(?P<image>.*?)".*?>.*?.*?【种子名称】:(?P<torrent>.*?)'
    r'【下载网址】: <a\s+href="(?P<url>.*?)"',
    re.DOTALL
)

# Find all matches
matches = pattern.finditer(text)
# Process each match and print the results
for match in matches:
    info = match.groupdict()
    print(f"Title: {info['title']}")
    print(f"Name: {info['name']}")
    print(f"Format: {info['format']}")
    print(f"Subtitle: {info['subtitle']}")
    print(f"Code: {info['code']}")
    print(f"Size: {info['size']} GB")
    print(f"Hash: {info['hash']}")
    print(f"Deadline: {info['deadline']}")
    print(f"Image Link: {info['image']}")
    print(f"Torrent: {info['torrent']}")
    print(f"Download URL: {info['url']}")
    print("="*50)




