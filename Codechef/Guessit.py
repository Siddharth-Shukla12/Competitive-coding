# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:55:00 2021

@author: siddh
"""
#https://www.codechef.com/problems/GUESIT99
try:
    l=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    fi=[]
    for _ in range(int(input())):
        N=int(input())
        N=(N%7+6)%7
        fi.append(l[N])
    for k in fi:
        print(k)
        
except:
    pass
