# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:09:34 2021

@author: siddh

"""
try:
    fi=[]
    for _ in range(int(input())):
        N,a,b=list(map(int,input().split()))
        S=0
        A=0
        for _ in range(N):
            c=str(input())
            d=[i for i in "EQUINOX"]
            
            if c[0] in d:
                S+=a
            else:
                A+=b
        if S>A:
            fi.append("SARTHAK")
        elif A>S:
            fi.append("ANURADHA")
        else:
            fi.append("DRAW")
    for k in fi:
        print(k)
except:
    pass