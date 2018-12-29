# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:09:32 2018

@author: 达内
"""

import urllib.request
import urllib.parse
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
baseurl = 'http://www.baidu.com/s?'
key = input('请输入要搜索的内容:')
key = urllib.parse.urlencode({'wd':key})
url = baseurl + key
res = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(res).read().decode('utf-8')

with open('美女.html','w',encoding='gb18030') as f:
    f.write(html)