# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:32:35 2021

@author: siddh
"""
#https://www.codechef.com/START5B/problems/BLITZ3_2
# cook your dish here
for _ in range(int(input())):
    N,A,B=list(map(int,input().split()))
    X=2*(180+N)
    print(X-(A+B))