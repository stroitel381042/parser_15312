import json
from PIL import Image
from io import BytesIO
import img as img
from bs4 import BeautifulSoup
import requests
import lxml

response = ["машины"]
url = "https://tap.az/elanlar/neqliyyat/ehtiyyat-hisseleri-ve-aksesuarlar?p%5B798%5D=7693"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
    }

r = requests.get(url=url, headers=headers)

#b = r.status_code
#b = r.request.headers
#print(b)

soup = BeautifulSoup(r.text, "lxml")
article_title = soup.find_all("div", class_="products-i rounded")
#print(article_title)
#soup_jpeg = BeautifulSoup(r.text, "html.parser")
#print(soup_jpeg)

print("=" * 100)

for article in article_title:

    article_name = article.find("div", class_="products-name").text
    # article_price = article.find("span", class_="s-item__detail s-item__detail--primary").text.strip()
#    article_url = article.find("a", class_="listing-item__link").get("href")
#    article_img = article.find("img").get("src")
#     #article_desc = article.find("div", class_="ramka").text.strip()
    print(article_name)
#
#
# #get_first_news()

print("=" * 100)

#with open("page_site#1", "w",encoding='UTF-8') as file:
#    file.write(str(soup))