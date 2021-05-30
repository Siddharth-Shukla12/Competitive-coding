# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:06:47 2021

@author: siddh
"""
#https://www.codechef.com/START4C/problems/CORTSENT
try:
    L1=[chr(i) for i in range(97,110)]
    L2=[chr(i) for i in range(78,91)]
    def identify(k):
        d=[]
        for c in k:
            if c in L1:
                d.append(1)
            elif c in L2:
                d.append(2)
            else:
                d.append(-1)
        d=list(set(d))
        if -1 in d or len(d)!=1:
            return -1
        return 1
    for _ in range(int(input())):
        n,*W=list(input().split())
        f=[]
        for i in W:
            g=identify(i)
            f.append(g)
        if -1 in f:
            print('NO')
        else:
            print('YES')
except:
    pass