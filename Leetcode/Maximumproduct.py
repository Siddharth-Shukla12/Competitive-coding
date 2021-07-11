# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:09:17 2021

@author: siddh
"""
#https://leetcode.com/contest/weekly-contest-247/problems/maximum-product-difference-between-two-pairs/
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return ((nums[n-1]*nums[n-2])-(nums[0]*nums[1]))