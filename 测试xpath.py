import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
url = "http://www.b520.cc/"
rep = requests.get(url =url,headers=headers).text
html = etree.HTML(rep)
# xp = '//*[@id="wrapper"]/div[3]/text()' # xpath直接拷贝的
new_xp = "//*[@id='wrapper']/div[2]/ul/li/a/@href" # 自己找的xpath
nav = html.xpath(new_xp)
print(nav)

# new_xp = "//*[@id='wrapper']/div[2]/ul/li/a/text()"

