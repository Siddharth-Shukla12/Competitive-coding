# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:58:10 2021

@author: siddh
"""
#https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        l=[ord(str(i)) for i in range(10)]
        m=''
        s=s.strip()
        for i in range(len(s)):
            if i==0:
                if s[i]=='+':
                    m+=s[i]
                elif s[i]=='-':
                    m+=s[i]
                elif ord(s[i]) in l:
                    m+=s[i]
                else:
                    break
            else:
                if ord(s[i]) in l:
                    m+=s[i]
                else:
                    break
        
                    
        try:
            i=int(m)
            
        except:
            return 0
        
        
        if i >(2**31 -1):
            return (2**31)-1
        elif i< (-1*(2**31)):
            return (-1*(2**31))
        else:
            return i