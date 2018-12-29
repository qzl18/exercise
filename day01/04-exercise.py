# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:45:44 2018

@author: 达内
"""

import urllib.request
import urllib.parse
import random
hlist = [{"User-Agent":'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}]

baseurl = 'https://tieba.baidu.com/f?'
name = input('请输入贴吧名称:')
begin = int(input('请输入起始页:'))
end = int(input('请输入终止页:'))
kw = urllib.parse.urlencode({'kw':name})

for page in range(begin,end+1):
    headers = random.choice(hlist)
    pn = str((page-1)*50)
    url = baseurl + kw + "&pn=" + pn
    req = urllib.request.Request(url,headers= headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    with open(name+'_'+str(page)+".html",'w',encoding='utf-8') as f:
        f.write(html)
    print('第%d页爬取成功'%page)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
