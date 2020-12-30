#正则表达式
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
# url="https://zhuanlan.zhihu.com/p/75647632"
# html=urlopen(url)
# bs=BeautifulSoup(html.read(),'lxml')
# imgList=bs.findAll('span',{'class':re.compile(".+p")})
# for i in imgList:
#     print(i)



filename="C:\\Users\\TZY\\Desktop\\SpiderTest\\"
url1="https://www.pixiv.net/artworks"
html=urlopen(url1)
bs=BeautifulSoup(html.read(),'lxml')
imglist=bs.findAll('img',{'alt':re.compile("我是正则表达式")})

count=0
for i in imglist:
    imgsrc=i.get('src')
    r = requests.get(imgsrc)
    if r.status_code == 200:
        with open(filename+str(count)+".jpg", 'wb') as f:
            f.write(r.content)
            f.close()
            print("差不多得了")
            count+=1
            print(count)
    else:
        print("error"+imgsrc)
