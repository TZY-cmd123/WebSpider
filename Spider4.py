#根据链接递归访问所有网站
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6/141728?fromtitle=BJTU&fromid=11227339&fr=aladdin'
html=urlopen(url)
bs=BeautifulSoup(html,'lxml')
for link in bs.findAll('a',{'href':re.compile('http://.+')}): # 找到所有的网址
    try:
        print(link['href'])
    except KeyError as e:
        print("关键字不匹配")