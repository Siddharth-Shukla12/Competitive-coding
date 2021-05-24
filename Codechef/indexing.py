# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:44:31 2021

@author: siddh
"""
#https://www.codechef.com/problems/INDX12
for _ in range(int(input())):
    a=input()
    l=[(ord(i)-96) for i in a]
    if sum(l)%2==0:
        print('YES')
    else:
        print('NO')