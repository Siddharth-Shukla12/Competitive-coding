# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:09:34 2021

@author: siddh

"""
try:
    def heaven(a):
        one=a.count("1")
        per=one/len(a)
        per=per*100
        if per>=50:
            return True
        else:
            return False
        
    def main():
        fi=[]
        for _ in range(int(input())):
            flag=0
            n=int(input())
            s=str(input())
            for i in range(1,len(s)):
               if heaven(s[0:i]):
                    flag=1
                    break
               else:
                   continue
            if flag==1:
                fi.append("YES")
            else:
                fi.append("NO")
        for k in fi:
            print(k)
    main()
except:
    pass
    
