# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:56:27 2018

@author: 达内
"""

import urllib.request
import re
import csv
class MaoyanSpider():
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"}
        self.baseurl = "https://maoyan.com/board/4?offset="
       
        
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
        
    def parsePage(self,html):
        p = re.compile('<p class="name".*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p> ',re.S)
        rList = p.findall(html)
        self.writeToCSV(rList)
        
    def writeToCSV(self,rList):
        for i in rList:
            i = list(i)
            with open ("猫眼.csv","a",newline="",encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(i)
                
        
    def workOn(self):
        for i in range(1,11):
            url = self.baseurl + str((i-1) * 10)
            self.getPage(url)
        
        
if __name__ =="__main__":
    spider = MaoyanSpider()
    spider.workOn()
    
    
