# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:31:09 2018

@author: 达内
"""

#import urllib.request
#url = 'http://www.baidu.com/'
#headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"}
#req = urllib.request.Request(url,headers=headers)
#res =urllib.request.urlopen(req)
#html = res.read().decode("utf-8")
#print(html)
import urllib.parse
s = (urllib.parse.urlencode({'wd':"美女"}))
baseurl = 'http://www.baidu.com/s?'
print(baseurl+s)