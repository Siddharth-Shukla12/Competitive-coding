# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:01:09 2021

@author: siddh

"""
#https://www.codechef.com/problems/LAZYCHF
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    print(min(a*b,a+c))