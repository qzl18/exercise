# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:47:59 2018

@author: 达内
"""
import urllib.request
import urllib.parse

class BaiduSpyder():
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com/f?"
        self.headers = {}
        
    #获取页面内容
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html
    #解析页面
    def parsePage(self):
        pass
    
    #保存数据
    def writePage(self,filename,html):
        with open(filename,'w',encoding="utf-8") as f:
            f.write(html)
    
    #主函数
    def workOn(self):
        name = input('请输入贴吧名称:')
        begin = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        kw = urllib.parse.urlencode({'kw':name})
        
        for page in range(begin,end+1):
            headers = random.choice(hlist)
            pn = str((page-1)*50)
            url = self.baseurl + kw + "&pn=" + pn
            file_name = '第'+str(page)+'页.html'
            html = self.getPage(url)
            self.writePage(file_name,html)
            print('第%d页爬取成功'%page)
    
    
if __name__ == "__main__":
    spyder = BaiduSpyder()
    spyder.workOn()
    
    
    