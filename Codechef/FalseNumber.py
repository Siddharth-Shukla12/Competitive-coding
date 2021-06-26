# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:09:12 2021

@author: siddh
"""
#https://www.codechef.com/LTIME97C/problems/FALSNUM/
try:
    for _ in range(int(input())):
        
        l=[str(i) for i in input()]
        if int(l[0])==1:
            l.insert(1,'0')
        else:
            l.insert(0,'1')
        print(int(''.join(l)))
except:
    pass