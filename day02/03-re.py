# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 10:14:45 2018

@author: 达内
"""
import re

html = '''
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    
    <p class="content">
        Small white rabbit white and white
    </p>
</div>
'''
p = re.compile('title="(.*?)".*<p class="content">(.*?)</p>',re.S)
print(p.findall(html))













