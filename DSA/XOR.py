# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:26:11 2021

@author: siddh
"""



def fun(a,b,p):
    
    count=1
    while  b>0:
        if b&1:
            count=(count*a)%p
        b=b>>1
        a=(a**2)%p
    return count
    
fi=[]
for _ in range(int(input())):
    N=int(input())
    p=1000000007
    c=2
    ans=fun(2,N-1,p)
    
    fi.append(ans)
            
for k in fi:
    print(k)