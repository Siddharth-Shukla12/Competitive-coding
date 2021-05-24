# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:41:35 2021

@author: siddh
"""
# https://www.codechef.com/TCFL2021/problems/TCFL21B
try:
    fi=[]
    for _ in range(int(input())):
        n=int(input())
        s1=str(input())
        s2=str(input())
        a=int(s1,2)
        b=int(s2,2)
        e1=0
        o1=0
        e2=0
        o2=0
        if (a^b)%2==0:
                while (a^b)%2==0:
                    a=a//2
                    o1+=1
                a=int(s1,2)
                while (a^b)%2==0:
                    b=b//2
                    o2+=1
                o=min(o1,o2)
                
                fi.append((0,o))
        else:
                while (a^b)%2!=0:
                    a=a//2
                    e1+=1
                a=int(s1,2)
                while (a^b)%2!=0:
                    b=b//2
                    e2+=1
                e=min(e1,e2)
                
                fi.append((e,0))
    for (i,j) in fi:
        print(i,j)
except:
    pass
            