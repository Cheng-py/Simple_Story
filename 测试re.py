import re


text = "第一asdasd章"
text2 = "sdadaad"

# if (re.match(re_p,text)):
#     print(True)
# testa = "123456789ABCD"
# testa = list(testa)
# print(testa[9:-1])

a = 10
b = float(2.3)
# print(a>b)
r_p = r"[\u7b2c](.|\n)*[\u7ae0]"
# r_p = r"[\u7ae0]"
# if (re.match(r_p,text)):


# if(text.startswith("第")and text.endswith("章")):
#     print(True)
#
# else:
#     print(False)

str ='英国记者<a target="_blank" href="https://baike.baidu.com/item/%E5%A4%A7%E5%8D%AB%C2%B7%E5%B8%95%E6%8B%89%E4%B8%81%C2%B7%E5%BC%97%E7%BD%97%E6%96%AF%E7%89%B9">大卫·弗罗斯特</a>逝世'

res = re.sub('<.*?>','',str)
print(res)
