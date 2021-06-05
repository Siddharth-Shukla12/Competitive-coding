# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 01:32:12 2021

@author: siddh
"""
#https://www.codechef.com/JUNE21C/problems/COCONUT/
try:
    for _ in range(int(input())):
        xa,xb,Xa,Xb=list(map(int,input().split()))
        if Xa%xa!=0:
            A=(Xa//xa)+1
        else:
            A=(Xa//xa)
        if Xb%xb!=0:
            B=(Xb//xb)+1
        else:
            B=(Xb//xb)
        print(A+B)
except:
    pass
    