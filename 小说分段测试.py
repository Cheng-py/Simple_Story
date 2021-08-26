import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
url = "http://www.b520.cc/chuanyuexiaoshuo/"

def next_html(url,headers):
    xpath_book = '//*[@id="newscontent"]/div[2]/ul/li/span/a/text()' #书名称
    xpath_url = '//*[@id="newscontent"]/div[2]/ul/li/span/a/@href' #书的url
    xpath_id = '//*[@id="newscontent"]/div[2]/ul/li/span/text()' #小说作者

    rep = requests.get(url=url,headers=headers).text
    # print(rep)
    html = etree.HTML(rep)
    r_book = html.xpath(xpath_book)
    r_id = html.xpath(xpath_id)
    r_url = html.xpath(xpath_url)
    BookAndId = dict(zip(r_book,r_id))
    BookAndUrl = dict(zip(r_book,r_url))
    print(r_book)
    try:
        s_book = input("============请输入你想要看的小说全称============"+"\n")
        s_url = BookAndUrl[s_book]
        print(s_url)
    except:
        KeyError(print("输入有误"))
        return False
next_html(url=url,headers=headers)