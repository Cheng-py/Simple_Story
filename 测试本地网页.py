from lxml import etree

text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
html=etree.HTML(text) #初始化生成一个XPath解析对象
xr = "/li"
html1 = html.xpath(xr)
print(html1)
result=etree.tostring(html,encoding='utf-8')   #解析对象输出代码
print(type(html))
print(type(result))
print(result.decode('utf-8'))
xpath_url = '//*[@id="newscontent"]/div[2]/ul/li/span/a/@href' #书的url
xpath_id = '//*[@id="newscontent"]/div[2]/ul/li/span/text()' #小说作者