import requests
from lxml import etree
import os
import re
import time
import datetime

def main_html(url,headers):    # 获取首页小说分类地址
    nav_name_href = "//*[@id='wrapper']/div[2]/ul/li/a//@href"
    response = requests.get(url,headers=headers).text
    html = etree.HTML(response)
    nav_name  = html.xpath(nav_name_href)[2:-1]
    return nav_name   #返回首页小说分类地址

def next_html(url,headers):                           # 该分类下的热门小说
    xpath_book = '//*[@id="newscontent"]/div[2]/ul/li/span/a/text()'  # 书名称
    xpath_url = '//*[@id="newscontent"]/div[2]/ul/li/span/a/@href'  # 书的url
    xpath_id = '//*[@id="newscontent"]/div[2]/ul/li/span/text()'  # 小说作者
    name_url = []                              # 用来存放小说的名称与地址
    rep = requests.get(url=url,headers=headers).text
    html = etree.HTML(rep)
    r_book = html.xpath(xpath_book)
    r_url = html.xpath(xpath_url)
    BookAndUrl = dict(zip(r_book,r_url))
    print(r_book)
    try:
        s_book = input("============请输入你想要看的小说全称============"+"\n")
        s_url = BookAndUrl[s_book]
        name_url.append(s_book)
        name_url.append(s_url)
        return name_url  # 获取想要的书名与地址,用列表返回
    except:
        KeyError(print("输入有误"))
        return False


def story_html(url, headers):   # 小说章节与url
    xpath_text = '//*[@id="list"]/dl/dd//text()'
    xpath_url = '//*[@id="list"]/dl/dd//a/@href'
    rep = requests.get(url=url,headers=headers).text
    html = etree.HTML(rep)
    x_text = html.xpath(xpath_text)
    x_url = html.xpath(xpath_url)
    text_dict = dict(zip(x_text[9:-1],x_url[9:-1])) # 去除掉章节前的话语导语之类的。
    return text_dict


def download_html(bookname,url_name_dict):
    num_d = 0   # 用来给下载文件编号排序。
    title_Re = r"[\u7b2c](.|\n)*[\u7ae0]"  # 匹配正确的章节名称。以第开头，章结尾
    key_count = len(url_name_dict.keys())    # 文章总数
    for key,values in url_name_dict.items():
        time.sleep(0.5)       # 设置休眠时间，防止下载过快内容为空,下载时候看着舒服一点。
        rep = requests.get(url=values,headers=headers).text
        html = etree.HTML(rep)
        xpath2 ='//*[@id="content"]//text()'
        the_end = html.xpath(xpath2)
        res = str(the_end)
        r = re.findall(u'[\u4e00-\u9fa5].+?', res) # 匹配中文，去除掉下载时候的其他转义字符，原生字符
        the_fi = "".join(r)
        the_final = list(the_fi)

        if not os.path.exists(os.getcwd() + "\\" + bookname): # 以小说名创建文件夹
            os.makedirs(os.getcwd() + "\\" + bookname)
        if (re.match(title_Re,key)):  # 获取所有有效章节
            num_d += 1
            try:
                with open(os.getcwd() + "\\" + bookname + "\\" + str(num_d)+key + ".txt", "w+", encoding="utf-8") as fp:
                    for num in range(len(the_final)):   # 每50个字换行一次，随自己调
                        if(num%50==0 and num!=0):
                            fp.write("\n" + the_final[num])
                        else:
                            fp.write(the_final[num])
                    print("{:10}{:>15}{:>20}".format(key,"下载成功","已完成:"+str(num_d)+"/"+str(key_count)))

            except (TimeoutError,IndexError):
                pass
        else:
            key_count = key_count -1
            print("{:10}{:>15}".format(key,"无效章节","已完成"))


def main_menu():
    num = input("""
                           ========================按数字输入想看的小说类型========================
                   1.玄幻小说    2.修真小说    3.都市小说    4.穿越小说    5.网游小说    6.科幻小说    7.言情小说
               """)
    return num

def is_num(num):  # 用来判断输入是否合格
    try:
        new_num = float(num)-1
        if(float(new_num)):
            try:
                if(float(num)>7):
                    return False
                elif(float(new_num)<=0):
                    return False
            except IndexError:
                pass
    except (ValueError,IndexError):
        pass
    try:
        import unicodedata
        unicodedata.numeric(num)
        return True
    except (TypeError, ValueError,IndexError):
        pass

    return False

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main_url ="http://www.b520.cc/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    num = main_menu() # 拿到想看的小说类型
    main_text_url = main_html(url=main_url,headers=headers)  # 地址。
    if(is_num(num)): # 判断输入数字合不合格。
        num =int(num)
        num = num-1
        text_2_url = main_text_url[num]
        text_2_url = "http://"+ text_2_url[2:-1]+"/"
        next_url = next_html(text_2_url, headers=headers)
        next_3 =story_html(next_url[1],headers=headers)
        download_html(next_url[0], next_3)
    end_time = datetime.datetime.now()
    print("############################共耗时%ss############################" % (end_time-start_time))



