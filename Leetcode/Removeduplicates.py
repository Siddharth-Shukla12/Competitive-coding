# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:53:37 2021

@author: siddh
"""
#https://leetcode.com/submissions/detail/511068482/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        new=list(set(nums))
        new.sort()
        for i in range(len(new)):
            nums[i]=new[i]
        
        return len(new)
            