# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:43:07 2021

@author: siddh
"""
#https://www.codechef.com/CAK22021/problems/BMPD
try:
    for _ in range(int(input())):
        N,X,Y,Z=list(map(int,input().split()))
        R1=10/X
        R2=5/Y
        R3=1/Z
        L=[R1,R2,R3]
        L.sort(reverse=True)
        d=dict()
        c=dict()
        d[10],d[5],d[1]=R1,R2,R3
        c[10],c[5],c[1]=X,Y,Z
        s=0
        for i,j in sorted(d.items(), key=lambda item: item[1],reverse=True):
            s+=(N//i)*c[i]
            
            if (N//i)!=0:
                N=N-(i*(N//i))
        print(s)   
except:
    pass
        
        