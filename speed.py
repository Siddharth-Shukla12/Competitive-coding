# -*- coding: utf-8 -*-
"""
Created on Wed May 26 01:44:39 2021

@author: siddh
"""
try:
    for _ in range(int(input())):
        U,V,A,S=list(map(int,input().split()))
        a=(U**2) - 2*A*S
        if a<=(V*V):
            print('Yes')
        else:
            print('No')
except:
    pass