# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:47:30 2021

@author: siddh
"""
#https://www.codechef.com/JUNE21C/problems/BITTUP
try:
    m=10**9+7
    for _ in range(int(input())): 
        n,k=map(int,input().split())
        ans=pow(2,n-1,m)+(pow(2,n-1,m)-1)
        print(int(pow(ans,k,m)))
except:
    pass