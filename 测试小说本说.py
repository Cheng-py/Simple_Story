import requests
from lxml import etree
import unicodedata as ucd
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
url = "http://www.b520.cc/0_7/2047.html"

rep = requests.get(url=url,headers=headers).text
html = etree.HTML(rep)
xp = '//*[@id="content"]//p//text()'
res = html.xpath(xp)
res = str(res)
r = re.findall(u'[\u4e00-\u9fa5].+?', res)
the_final="".join(r)
print(the_final)