# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:09:04 2021

@author: siddh
"""
#https://www.codechef.com/LTIME97C/problems/CHFRICH/
try:
    for _ in range(int(input())):
        A,B,X=list(map(int,input().split()))
        print((B-A)//X)
except:
    pass