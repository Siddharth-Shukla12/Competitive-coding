# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:00:46 2021

@author: siddh
"""
#https://www.codechef.com/SMCC2021/problems/LUCKY02
try:
    for _ in range(int(input())):
        a=int(input())
        l=[int(i) for i in str(a)]
        l=list(set(l))
        l.sort()
        if len(l)==1:
            if l[0]==3 or l[0]==7:
                print('LUCKY')
            else:
                print("BETTER LUCK NEXT TIME")
        elif len(l)==2:
            if l[0]==3 and l[1]==7:
                print('LUCKY')
            else:
                print("BETTER LUCK NEXT TIME")
        else:
            print("BETTER LUCK NEXT TIME")
except:
    pass