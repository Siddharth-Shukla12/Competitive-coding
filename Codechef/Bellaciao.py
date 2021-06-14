# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 01:53:48 2021

@author: siddh
"""
try:
    for _ in range(int(input())):
        D,d,P,Q=list(map(int,input().split()))
        R=D%d
        I=D//d
        n=I-1
        S=n*(n+1)//2
        L=(I*P)+S*Q
        Ans=(d*L)+R*(P+I*Q)
        print(Ans)
except:
    pass