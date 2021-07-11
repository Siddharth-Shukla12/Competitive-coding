# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:41:23 2021

@author: siddh
"""
#https://leetcode.com/submissions/detail/508732907/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]