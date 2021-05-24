# -*- coding: utf-8 -*-
"""
Created on Fri May 21 18:53:37 2021

@author: siddh
"""
#https://www.codechef.com/CDRL2021/problems/PR_PO
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    li=list(map(int,input().split()))
    b=b%a
    b=-1*b
    for k in (li[b:]+li[:b]):
        print(k,end=' ')
    
             