# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:12:29 2021

@author: siddh
"""
#https://leetcode.com/problems/candy/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        one=[1 for i in range(n)]
        c=0
    
        for i in range(n-1):
            if ratings[i]<ratings[i+1]:
                
                one[i+1]=max(1+one[i],one[i+1])
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                one[i]=max(1+one[i+1],one[i])
            
            
        return sum(one)