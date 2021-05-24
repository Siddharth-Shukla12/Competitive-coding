# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:45:53 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21A/
try:
    def main():
        fi=[]
        for _ in range(int(input())):
            R,C=list(map(int,input().split()))
            
            
            matrix=[]
            for i in range(R):          
                a=list(map(int,input().split()))
                if len(a)==C:     
                    matrix.append(a)
            
            e,f=R//2,C//2
            t=[]
            for i in range(R):
                for j in range(C):
                    if matrix[i][j]==0 :
                        s=abs(i-e)+abs(f-j)
                        t.append(s)
            if len(t)==0:
                fi.append(-1)
            else:
                g=min(t)
                fi.append(g)
        for k in fi:
            if k==-1:
                print('NO ',k)
            else:
                print('YES ',k)
    main()
except():
    pass
        
