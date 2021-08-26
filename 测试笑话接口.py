import requests
import json
pag = 0
# 用聚合
for i in range(1,21):
    pag+=1
    params ={
        "key":"",
        "sort":"desc",
        "page":i,
        "pagesize":20,
        "time":"1418816972"
    }
    print("第{}页".format(pag))
    rep = requests.get(url="",params=params)
    html = rep.json()
    res = html['result']
    end = res['data']
    num = 0
    for i in range(len(end)):
        num+=1
        print("第"+str(num)+"篇笑话"+end[i]['content'],end="\n")