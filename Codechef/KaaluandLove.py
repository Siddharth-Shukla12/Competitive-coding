# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:52:08 2021

@author: siddh
"""
#https://www.codechef.com/problems/WEEKFIND/
try:
    l=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    fi=[]
    for _ in range(int(input())):
        Day,N=list(input().split())
        N=int(N)
        c=l.index(Day)
        N=(N%7+c)%7
        fi.append(l[N])
    for k in fi:
        print(k)
        
except:
    pass
