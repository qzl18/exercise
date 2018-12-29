# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 20:14:16 2018

@author: 达内
"""

import urllib.request
import re
class LianjiaSpider():
    def __init__(self):
        self.headers = {"User-Agent":""}
        self.baseurl = "https://ty.lianjia.com/ershoufang/pg"
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
    def parsePage(self,html):
#        p = re.compile("",re.S)
#        rList = p.findall(html)
        rList=html
        self.writePage(rList)
    def writePage(self,rList):
        with open('a.txt','a',encoding="utf-8") as f:
            f.write(rList)
    def workOn(self):
        for i in range(1,2):
            url = self.baseurl+str(i)
            self.getPage(url)
            print("爬取%d页成功"%i)
            
if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.workOn()