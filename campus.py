# 抓取校花网 校花图片
# 作者：DYBOY 小东
# 时间：2017-09-06

'''
http://www.xiaohuar.com/list-1-0.html 第一页
http://www.xiaohuar.com/list-1-1.html 第二页

'''

import requests
import re

from bs4 import BeautifulSoup
#以上作为基本引用


def getGirls(girl_url):
    main_url = 'http://www.xiaohuar.com'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    res = requests.get(girl_url,headers = header,timeout=10)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text,'html.parser')
    for images in soup.select('.item'):
        img_url = main_url + images.select('.item_t .img a img')[0]['src']
        houzhui = img_url[-4:]
        img_alt = images.select('.item_t .img a img')[0]['alt'] + houzhui
        print(img_alt)
        img = requests.get(img_url)
        with open('xiaohua/' + img_alt,"wb") as code:
            code.write(img.content)
    print('ok!')

def url_change():
    for i in range(19,44):
        url = 'http://www.xiaohuar.com/list-1-' + str(i) + '.html'
        getGirls(url)


#MAIN
url_change()
