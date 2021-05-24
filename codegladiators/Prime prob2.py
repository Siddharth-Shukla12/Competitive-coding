# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:11:53 2021

@author: siddh
"""


#https://www.techgig.com/codegladiators/dashboard   problem 2   
def isprime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True   
def nprime(a,b):
    
    a1=[i for i in range(a,b+1)]
    a1.sort()
    mi=0
    ma=0
    
    for i in a1:
        if isprime(i):
            mi=i
            
            break
    for i in a1[::-1]:
        if isprime(i):
            
            ma=i
            
            break
            
    
    if mi==0 and ma==0:
        return -1
    else:
        return (ma-mi)
def main():
    fi=[]
    for i in range(int(input())):
        a,b=list(map(int,input().split()))
        fi.append(nprime(a,b))
    for k in fi:
        print(k)
main()
