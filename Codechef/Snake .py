# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:06:21 2021

@author: siddh
"""
# https://www.codechef.com/TCFL2021/problems/TCFL21A
try:
    def main():
        fi=[]
        for _ in range(int(input())):
            K,M=list(map(int,input().split()))
            x=list(map(int,input().split()))
            y=list(map(int,input().split()))
            a=list()
            b=list()
            for l in x:
                a.append(l)
            for m in y:
                b.append(m)
            
            li=list(zip(x,y))
            
            sum=0
            for i in range(len(li)-1):
                sum+=abs(li[i][0]-li[i+1][0])+abs(li[i][1]-li[i+1][1])
            sum+=abs(li[i][0])+abs(li[i][1])
            
            if sum<M:
                fi.append('Yes')
            else:
                fi.append('No')
        for t in fi:
            print(t)
    main()
except:
    pass