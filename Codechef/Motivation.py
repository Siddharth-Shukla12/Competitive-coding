# -*- coding: utf-8 -*-
"""
Created on Wed May 26 01:33:43 2021

@author: siddh
"""
#https://www.codechef.com/LTIME94C/problems/IMDB
try:
    for _ in range(int(input())):
        N,X=list(map(int,input().split()))
        a=[]
        for j in range(N):
            S,R=list(map(int,input().split()))
            if S<=X:
                a.append(R)
        print(max(a))
except:
    pass