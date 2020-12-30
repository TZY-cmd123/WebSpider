from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://zhuanlan.zhihu.com/p/75647632')
bs=BeautifulSoup(html.read().decode('utf-8'),'lxml')
nameList=bs.findAll('span',{'class':'kn'})#找到所有符合要求的span
print(nameList)
for name in nameList:
    print(name.get_text())


nameList=bs.findAll('code')#找到所有的code,默认是递归查找，也可以设置成非递归
print(nameList)
for name in nameList:
    print(name.get_text())#其中get_text()是获得文本结构，即清除标签





