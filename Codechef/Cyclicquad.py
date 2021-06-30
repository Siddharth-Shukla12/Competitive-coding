# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:59:31 2021

@author: siddh
"""
#https://www.codechef.com/START5B/problems/CYCLICQD/
for _ in range(int(input())):
    A,B,C,D=list(map(int,input().split()))
    if (A+C)==180 and (B+D)==180:
        print('Yes')
    else:
        print('No')