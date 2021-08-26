from lxml import etree
import requests
response = requests.get('https://mil.news.sina.com.cn/')
response.encoding="utf-8"
txt = response.text
html = etree.HTML(txt)
result = html.xpath('//div[@class="zgjq"]/div[@class="left"]//ul[1]//a')
for li in result:
    title = li.xpath('./text()')
    if len(title):
        print (title[0]),
        print (li.xpath('./@href'))