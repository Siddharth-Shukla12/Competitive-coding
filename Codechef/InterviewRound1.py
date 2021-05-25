# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:36:50 2021

@author: siddh
"""
#https://www.codechef.com/SMCC2021/problems/CODE004
try:
    for _ in range(int(input())):
        s=input()
        a=['C','o','D','e']
        flag=0
        for i in a:
            if i not in s:
                flag=1
                break
        
        if flag==0:
            if 'E' in s[1:-1] and 'e' in s[1:-1]:
                print('SELECTED')
            else:
                print('REJECTED')
        else:
            print('REJECTED')
                
        
      

except:
    pass