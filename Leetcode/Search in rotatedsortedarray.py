# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:13:21 2021

@author: siddh
"""
#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
         if target in nums:
            return nums.index(target)
         else:
            return -1
            