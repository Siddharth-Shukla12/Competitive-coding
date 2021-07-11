# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:08:08 2021

@author: siddh
"""
#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)
        area=[]
        cap=0
        while (j-i)>=2:
            c=min(height[i],height[j-1])*((j-i)-1)
            if c>cap:
                cap=c
            if height[i]<=height[j-1]:
                i+=1
            else:
                j-=1
        return cap