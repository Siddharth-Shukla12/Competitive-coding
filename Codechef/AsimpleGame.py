# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:48:00 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21D
try: 
   def me(a):
        
        i=0
        
        
        li=[]
        for i in range(len(a)):
            if i!=len(a)-1 and a[i]==a[i+1] :
                
                continue
            
            
            else:
                li.append(a[i])
        return li
   def main():
        
       
        fi=[]
        for _ in range(int(input())):
            count0,count1=0,0
            R,C=list(map(int,input().split()))
            
            
            matrix=[]
            for i in range(R):          
                a=list(map(int,input().split()))
                if len(a)==C:     
                    matrix.append(a)
            
            for i in range(R):
                matrix[i]=me(matrix[i])
            for i in matrix:
                for j in i:
                    if j==1:
                        count1+=1
                    elif j==0:
                        count0+=1
            if count0<=count1:
                fi.append('CHEF')
            else:
                fi.append('APOLLO')
        for l in fi:
            print(l)                   
   main()
except:
    pass    