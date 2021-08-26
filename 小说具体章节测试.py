
import re
import requests
from lxml import etree

url = "http://www.b520.cc/52_52542/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


def select_story(url,headers):
    x_text = r".[第]"
    xpath_text = '//*[@id="list"]/dl/dd//text()'
    xpath_url = '//*[@id="list"]/dl/dd//a/@href'
    rep = requests.get(url=url,headers=headers).text
    html = etree.HTML(rep)
    xtext = html.xpath(xpath_text)
    xurl = html.xpath(xpath_url)
    text_dict = dict(zip(xtext[9:-1],xurl[9:-1]))
    return text_dict

select_story(url,headers)