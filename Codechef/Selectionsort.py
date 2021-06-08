# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:39:59 2021

@author: siddh
"""
l=list(map(int,input().split()))



a=l
 



for j in range(len(a)):
    min=j
    for i in range(j+1,len(a)):
        
        if a[min]>a[i]:
            min=i
            
    
    a[j],a[min]=a[min],a[j]
for k in a:
    print(k,end=' ')
    
    
