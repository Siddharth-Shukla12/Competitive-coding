# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:22:29 2021

@author: siddh
"""
#https://www.codechef.com/MISC2021/problems/MCQ3
try:
    N,M=list(map(int,input().split()))
    L=list(map(int,input().split()))
    c=M
    flag=1
    for i in range(N-1):
        if L[i]>L[i+1]:
            c+=(L[i]-L[i+1])
            
        elif L[i+1]>L[i]:
            d=L[i+1]-L[i]
            if d<=c:
                c=c-d
                
            else:
                flag=0
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
except:
    pass
                