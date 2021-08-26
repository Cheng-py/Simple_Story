import requests as re
from lxml import etree

file = open('saye.txt', 'w', encoding='utf-8')
url = 'https://www.bqg8.la/57_57576/25070353.html'
chapter = 1
chapterNum = 150

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}


def getContent():
    global url, chapter
    response = re.get(url, headers=header)
    response.encoding = 'gbk'

    data = etree.HTML(response.text)

    file.write("\n\n第{0}章\n".format(chapter))
    chapter += 1

    str = data.xpath('string(//div[@id="content"])')
    file.write('\n    '.join(str.split()))

    url = data.xpath('//a[text()="下一章"]/@href')[0]
    print(url)


if __name__ == '__main__':
    for i in range(chapterNum):
        getContent()

file.close()