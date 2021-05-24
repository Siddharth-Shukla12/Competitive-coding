# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:42:52 2021

@author: siddh
"""
#https://www.codechef.com/NERD2021/problems/DN003/
n=int(input())
l=list(map(int,input().split()))
a=[]
count=0
for i in range(n):
    if l[i]==0:
       l=[l[j] if j<i else 1 if l[j]==0 else 0 for j in range(n)]
       count+=1
print(count)