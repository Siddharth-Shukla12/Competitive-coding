# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:15:26 2021

@author: siddh
"""
#https://www.codechef.com/problems/COLLECT0
for _ in range(int(input())):
    A,B=list(map(int,input().split()))
    if (A*.2)>(B*.2):
        print("A")
        
    else:
        print("B")
   