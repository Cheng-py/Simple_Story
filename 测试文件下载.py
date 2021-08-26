import os
import requests
from lxml import etree
import re
text = ['武动乾坤结局感言以及新书', '第一章 北灵院', '第二章 被踢出灵路的少年']
url2 = ['http://www.b520.cc/0_7/2046.html', 'http://www.b520.cc/0_7/2047.html']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

all = dict(zip(text,url2))
a = "http://www.b520.cc/xuanhuanxiaoshuo/"
b = "http://www.b520.cc/4_4612/"

def download_html(bookname,test_dict):
    for key,values in test_dict.items():
        rep = requests.get(url=values,headers=headers).text
        html = etree.HTML(rep)
        xpath2 ='//*[@id="content"]//text()'
        the_end = html.xpath(xpath2)
        res = str(the_end)
        r = re.findall(u'[\u4e00-\u9fa5].+?', res)
        the_fi = "".join(r)
        the_final = list(the_fi)
        if not os.path.exists(os.getcwd() + "\\" + bookname):
            os.makedirs(os.getcwd() + "\\" + bookname)
        with open(os.getcwd() + "\\" + bookname + "\\" + key + ".txt", "a", encoding="utf-8") as fp:
            for num in range(len(the_final)):
                if(num%100==0 and num!=0):
                    fp.write("\n"+ the_final[num])

                else:
                    fp.write(the_final[num])

download_html("大主宰",all)













