# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 09:55:20 2018

@author: 达内
"""

import re
s = "A B C D"
p1 = re.compile("\w+\s+\w+")
print(p1.findall(s))
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
