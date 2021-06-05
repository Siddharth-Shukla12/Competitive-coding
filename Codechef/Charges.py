# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 01:30:16 2021

@author: siddh
"""
#https://www.codechef.com/LTIME96B/problems/CHARGES/
try:
    def dis(s):
        su=0
        for m in range(len(s)-1):
            if s[m]!=s[m+1]:
                su+=1
            else:
                su+=2
        return su
                    
        
    for _ in range(int(input())):
        N,K=list(map(int,input().split()))
        s=[int(i) for i in input()]
        L=list(map(int,input().split()))
        k=dis(s)
        if N==1:
            print(0)
        else:
            for j in L:
                if (j-1)!=0 and (j-1)!=(len(s)-1):
                    if s[j-2] !=s[j-1]:
                        k+=1
                    if s[j-2]==s[j-1]:
                        k=k-1
                    if s[j]!=s[j-1]:
                        k+=1
                    if s[j]==s[j-1]:
                        k=k-1
                else:
                    if (j-1)==0:
                        if s[j]!=s[j-1]:
                            k+=1
                        else :
                            k=k-1
                    if (j-1)==(len(s)-1):
                        if s[j-2] !=s[j-1]:
                            k+=1
                        else:
                            k=k-1
                    
                if s[j-1]==0:
                    s[j-1]=1
                else:
                    s[j-1]=0
                print(k)
            
except:
    pass
         