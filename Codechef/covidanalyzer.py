# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:05:38 2021

@author: siddh
"""
#https://www.codechef.com/problems/COVIN
def fib(n):
    l=[1,2]
    x=l[0]
    y=l[1]
    for i in range(n-2):
        t=x+y
        l.append(t)
        x=y
        y=t
    return l
        
a=fib(90)
for _ in range(int(input())):
    n=int(input())
    print(a[n-1])