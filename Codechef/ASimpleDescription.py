# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:49:09 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21E
try:
    def ch(i):
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            return 1
        else:
            return 0
    def nu(i):
        if ord(i)>=48 and ord(i)<=57:
            return 1
        else:
            return 0
    def main():
        fi=[]
        for _ in range(int(input())):
            n=int(input())
            st=str(input())
            letter=[]
            num=[]
            ma=[]
           
            countn=0
            counts=0
            n=''
            c=''
            i=0
            
            while True:
                
                while i!=len(st)  and nu(st[i]) :
                    c=''
                    n+=st[i]
                    
                    
                    countn+=1
                    i+=1
                if len(n)!=0:
                    num.append(int(n))
                while i!=len(st)  and ch(st[i]):
                    n=''
                    c+=st[i]
                    counts+=1
                    i+=1
               
                if len(c)!=0:
                    letter.append(c)
                if i==len(st):
                    break
          
            
            for j in letter:
                ma.append(len(j))
            z=max(ma)
            for t in letter:
                if len(t)==z:
                    break
            fi.append((t,max(num)))
        for (d,f) in fi:
            print(d,end=' ')
            print(f)
                        
    main()
except:
    pass