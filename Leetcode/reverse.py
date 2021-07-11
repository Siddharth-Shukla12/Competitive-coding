# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:07:29 2021

@author: siddh
"""
l=list(input().split())

c1=0

c2=len(l)-1
while c2>=c1:
    l[c1],l[c2]=l[c2],l[c1]
    c1+=1
    c2-=1
print(l)

