# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:38:53 2021

@author: siddh
"""
#https://www.codechef.com/problems/DATE1
for _ in range(int(input())):
    A,Y,X=list(map(int,input().split()))
    if A<Y:
        print(1+A*X)
    elif A>=Y:
        print(Y*X)
