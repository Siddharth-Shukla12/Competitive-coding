# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:28:02 2021

@author: siddh

"""
try:
    fi=[]
    for _ in range(int(input())):
        n=int(input())
        li=list(map(int,input().split()))
        flag=0
        while True:
        
            for i in range(len(li)):
                if li[i]==0:
                    fi.append(i+1)
                    flag=1
                    break
                li=[t-1 if t!=0 else t for t in li]
            if flag==1:
                break
        
    for t in fi:
        print(t)
except:
    pass

    