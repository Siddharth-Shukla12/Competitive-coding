# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:43:34 2021

@author: siddh
"""
#https://www.codechef.com/problems/NOBEL
try:
    for _ in range(int(input())):
        N,M=list(map(int,input().split()))
        L=list(map(int,input().split()))
        L=list(set(L))
        L.sort()
        
        Q=[i for i in range(1,M+1)]
        Q=list(set(Q))
        Q.sort()
        if Q!=L:
            print('YES')
        else:
            print('NO')
          
except:
    pass