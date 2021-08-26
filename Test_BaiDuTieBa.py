import requests
from lxml import etree



url = "https://tieba.baidu.com/f?ie=utf-8&kw=DNF&fr=search"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

rep = requests.get(url,headers)
result = rep.text
html = etree.HTML(result)

x_u = './/div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()'
x_a = './/div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()'

xut = html.xpath(x_u)
xat = html.xpath(x_a)
all_ = dict(zip(xut,xat))
for key,value in all_.items():
    print("标题{}###作者{}".format(key,value))


        # html.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()')
        # item["Author"] = html.xpath('.//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()')


