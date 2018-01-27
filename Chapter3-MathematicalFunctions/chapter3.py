# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:12:51 2018

@author: Wey Yi
"""

import math

print('{:^5}  {:^5}  {:^5}  {:^5}  {:^5}'.format('i', 'int', 'trunk', 'floor', 'ceil'))
print('{:-^5}  {:-^5}  {:-^5}  {:-^5}  {:-^5}'.format('', '', '', '', ''))

fmt = '  '.join(['{:5.1f}'] * 5)

for i in range(20):
    print(fmt.format(i, int(i), math.trunc(i), math.floor(i), math.ceil(i)))