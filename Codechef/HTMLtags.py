# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:10:35 2021

@author: siddh
"""
#https://www.codechef.com/LTIME97C/problems/HTMLTAGS/
try:
    li1=[chr(i) for i in range(97,123)]
    li2=[chr(i) for i in range(48,58)]
    
    def isalnu(s):
        flag=1
        for i in s:
            if i in li1 or i in li2:
                continue
            else:
                flag=0
                break
        if flag==1:
            return True
        else:
            return False
    for _ in range(int(input())):
        
        l=input().strip()
        if len(l)>3 and l[0]=='<' and l[1]=='/' and l[-1]=='>' and isalnu(l[2:-1]):
            print('Success')
        else:
            print('Error')
except:
    pass
         
