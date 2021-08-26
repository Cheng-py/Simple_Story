

# list1 = list[1,2,3,4,5,6,7,8,9]
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
rep = requests.get("http://www.baidu.com",headers=headers)
html = rep.text
print(html)