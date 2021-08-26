

from lxml import etree
import requests
rep=requests.get('https://www.baidu.com')
html=etree.HTML(rep.text)
aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
print(aa)