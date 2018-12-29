# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 09:46:02 2018

@author: 达内
"""

import re
html = """<div><p>你好</p></div>
<div><p>你坏</p></div>"""
p = re.compile(r'<div><p>.*?</p></div>',re.S)
r= p.findall(html)
print(r) 