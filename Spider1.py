from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_html(url='http://www.pythonscraping.com/'):
    try:
        html=urlopen(url=url)
    except HTTPError as e:
        return '网络错误'+e
    try:
        bs=BeautifulSoup(html,'lxml')
        title=bs.body.h1#暂时捕捉body中的h1，其他的部分可以放在事后优化
    except AttributeError as e:
        return '捕捉错误'+e
    return title

print(get_html())







