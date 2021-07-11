# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:11:20 2021

@author: siddh
"""
#https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        substitute={1000: 'M', 900:'CM', 500: 'D', 400: 'CD', 100 :'C', 90 :'XC', 50 : 'L', 40 :'XL', 10:'X', 9:'IX', 5: 'V', 4: 'IV', 1: 'I'}
       
        ans=''
        for i,j in substitute.items():
            if i>num:
                continue
            while i<=num:
                ans+=j
                num=num-i
        return ans
        