# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:36:41 2021

@author: siddh
"""
#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for k in range(len(nums)):
            
            if ((target-nums[k]) in nums):
                if (nums.index(target-nums[k])!=k):
                    c=min(k,nums.index(target-nums[k]))
                    d=max(k,nums.index(target-nums[k]))
                    a.append(c)
                    a.append(d)
                    return a
                    break