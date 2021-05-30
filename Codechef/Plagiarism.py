# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:00:04 2021

@author: siddh
"""
#https://www.codechef.com/START4C/problems/QUIZPLAG
try:
    for _ in range(int(input())):
        N,M,K=list(map(int,input().split()))
        l=list(map(int,input().split()))
       
       
        
        fin=[]
        s1=set()
        s2=set()
        for p in l:
            if (p >=1 and p<=N):
                if p in s1:
                    s2.add(p)
                else:
                    s1.add(p)
                
        lst=list(s2)
        lst.sort()
    
        print(len(lst),end=' ')
        for i in lst:
            print(i,end=' ')
        print()
except:
    pass
        