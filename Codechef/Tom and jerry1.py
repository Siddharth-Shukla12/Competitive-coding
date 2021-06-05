# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 01:39:20 2021

@author: siddh
"""
#https://www.codechef.com/LTIME96B/problems/TANDJ1/
try:
    for _ in range(int(input())):
        a,b,c,d,K=list(map(int,input().split()))
        t= abs(a-c)+abs(b-d)
        flag=0
        if t>K:
            flag=1
            print('NO')
        if flag==0:
            
            t=(K-t)
            if t%2==0:
                print('YES')
            else:
                print('NO')
except:
    pass
        