# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:57:12 2021

@author: siddh
"""
#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        if numRows==1:
            return s
        else:
    
            F=[s[i] for i in range(0,n,((numRows-1)+(numRows-2)+1))]



            for i in range(1,numRows-1):
                j=i
                count=0
                while j<n:
                    F.append(s[j])
                    
                    if count%2==0:
                        j+=2*(numRows-(i+1))
                    else:
                        j+=(2*(i-1)+2)
                    count+=1
            L=[s[i] for i in range(numRows-1,n,((numRows-1)+(numRows-2)+1))]
            for k in L:
                F.append(k)
            return "".join(F)