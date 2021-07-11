# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:51:55 2021

@author: siddh
"""
#https://leetcode.com/contest/weekly-contest-246/submissions/detail/510430156/
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        num=int(num)
        while num!=0:
            if (int(num)&1)==1:
                return str(num)
            num=num//10
        return ""
            
         
        