# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:51:47 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21F/
try:
   def Fun(fish,x):
        for i in fish:
            x=i*x-(i//2)
        return x
   def main():
        fi=[]
        for _ in range(int(input())):
            n1=int(input())
            fish=list(map(int,input().split()))
            c=int(input())
            while c!=0:
                
            
                a,b=list(map(int,input().split()))
                good=0
                bad=0
            
                for g in range(a,b+1):
                    if Fun(fish,g)%2==0:
                        good+=1
                    else :
                        bad+=1
                fi.append((good,bad))
                c-=1
        for (j,k) in fi:
            print(j,end=' ')
            print(k)
   main()
except:
    pass