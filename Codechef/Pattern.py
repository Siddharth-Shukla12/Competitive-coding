# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:18:37 2021

@author: siddh
"""
#https://www.codechef.com/SMCC2021/problems/PATRN03
try:
    for _ in range(int(input())):
        n=int(input())
        for i in range(1,n+1):
            for l in range(i):
                for k in range(l):
                    print("*",end='')
                print(l+1,end='')
            print()
except:
    pass