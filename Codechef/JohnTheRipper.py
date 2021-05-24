# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:44:26 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21B/
# cook your dish here
try:
    def work(a):
        
        b=bin(a)[2:]
        c=[i for i in b]
        while len(c)!=7:
            c.insert(0,'0')
        if c[0]=='0':
            c[0]='1'
        else: 
            c[0]='0'
        c=''.join(c)
        h=int(c,2)
        if (h>=65 and h<=90) or (h>=97 and h<=122):
            return h
        else:
            return a
    def conv(li):
        for x in range(len(li)):
            li[x]=chr(li[x])
        return li
            
    def main():
        fi=[]
        for _ in range(int(input())):
            n=int(input())
            
            li=list(map(int,input().split()))
            if len(li)==n:
                for i in range(len(li)):
                    c=li[i]
                    li[i]=work(c)
                li=conv(li)
                fi.append(''.join(li))
        for v in fi:
            print(v)
    main()
except:
    pass