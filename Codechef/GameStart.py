# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:22:38 2021

@author: siddh
"""
#https://www.codechef.com/SMCC2021/problems/GAME01
try:
    for _ in range(int(input())):
        N,M=list(map(int,input().split()))
        l1=list(map(int,input().split()))
        l2=list(map(int,input().split()))
        a=list(set(l1))
        b=list(set(l2))
        c=[]
        for i in a:
            
            if l1.count(i)==1 and i%3==0:
                if i in b and l2.count(i)==1:
                    c.append(i)
        if len(c)!=0:
            c.sort()
            for k in c:
                print(k,end=' ')
        else:
            print(-1)
except:
    pass                