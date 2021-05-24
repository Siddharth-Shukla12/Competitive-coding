# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:33:22 2021

@author: siddh
"""
#https://www.codechef.com/problems/LETSC001
def sieve(n):
    l=[True for _ in range(n+1)]
    l[0],l[1]=False,False
    for i in range(2,int(n**.5)+1):
        for j in range(2*i,n+1,i):
            l[j]=False
    return l.count(True)
n=int(input())
print(sieve(n))