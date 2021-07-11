# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:39:36 2021

@author: siddh
"""
#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            x=x[1:]
            x=x[::-1]
            x=-1*int(x)
            
            
            
        else:
            x=x[::-1]
            x=int(x)
        if x>((2**31)-1) or x<(-1*(2**31)):
            return 0
        else:
            return x