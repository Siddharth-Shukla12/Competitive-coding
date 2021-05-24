# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:19:59 2021

@author: siddh
"""
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=min(l)
    print(n-l.count(a))