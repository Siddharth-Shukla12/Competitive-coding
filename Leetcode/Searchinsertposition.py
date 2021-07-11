# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:49:21 2021

@author: siddh
"""
#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        dec=nums
        if target in nums:
            return nums.index(target)
        else:
            l=len(nums)
            while nums[-1]>target:
                
                nums.pop()
                if len(nums)==0:
                    return 0
                l-=1
            return l
                