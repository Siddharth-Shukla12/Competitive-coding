# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:11:38 2021

@author: siddh
"""
#https://www.codechef.com/LTIME97C/problems/UNONE
from collections import deque
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li1=deque()
    li2=deque()
    for i in l:
        if i%2==0:
            li1.appendleft(i)
        else:
            li2.appendleft(i)
    for i in li1:
        print(i,end=' ')
    for i in li2:
        print(i,end=' ')
        
