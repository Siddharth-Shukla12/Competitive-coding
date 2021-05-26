# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:39:29 2021

@author: siddh
"""
#https://www.codechef.com/MISC2021/problems/MCQ2
try:
    n=int(input())
    l=[int(input()) for i in range(n)]
    z=[1 for i in l]
    for i in range(n-1):
        
        if l[i]>l[i+1]:
            if z[i]<=z[i+1]:
                z[i]=z[i+1]+1
        elif l[i]<l[i+1]:
            if z[i+1]<=z[i]:
                z[i+1]=z[i]+1
    
    print(sum(z))   
except:
    pass