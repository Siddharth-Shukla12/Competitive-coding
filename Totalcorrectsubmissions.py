# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:33:43 2021

@author: siddh
"""
#https://www.codechef.com/START5B/problems/TOTCRT
for _ in range(int(input())):
    n=int(input())
    d=dict()
    for i in range(3*n):
        li=list(input().split())
        if li[0] not in d.keys():
            d[li[0]]=int(li[1])
        else:
            d[li[0]]+=int(li[1])
    val=list(d.values())
    val.sort()
    for i in val:
        print(i,end=' ')
    print()