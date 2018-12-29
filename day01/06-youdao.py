# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:47:17 2018

@author: '达内
"""

import urllib.request
import urllib.parse
import json

key = input("请输入要翻译的内容:")
data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15458120987442',
        'sign': 'af53413198cb6faacef05e9f4642aae5',
        'ts': '1545812098744',
        'bv': '9c4fffad2fb69d08cd130e408e0f8108',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
        }
data = urllib.parse.urlencode(data).encode('utf-8')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
rDict = json.loads(html)
result = rDict.get("translateResult")[0][0].get('tgt')
print(result)
























