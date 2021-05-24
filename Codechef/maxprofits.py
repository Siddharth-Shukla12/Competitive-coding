# -*- coding: utf-8 -*-
"""
Created on Sat May 22 01:11:19 2021

@author: siddh
"""
#https://www.codechef.com/problems/LETSC004
n=int(input())
l=list(map(int,input().split()))
l.sort()
a=[]
for i in range(n):
     a.append(l[i]*(n-i))
print(max(a))