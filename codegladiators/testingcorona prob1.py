# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:34:59 2021

@author: siddh
"""
#https://www.techgig.com/codegladiators/dashboard  problem 1
def comp(V,S):
    i,j=0,0
    m=len(S)
    n=len(V)
    while j<m and i<n:
        if S[j]==V[i]:
            j=j+1
            
        i=i+1
        
    return j==m
def main():
    V=input()
    fi=[]
    
    for i in range(int(input())):
        
        s=input()
        if comp(V,s):
            fi.append("POSITIVE")
        else:
            fi.append("NEGATIVE")
    for k in fi:
        print(k)
main()
                    
                
    