# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:47:15 2021

@author: siddh
"""
#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        opening_symbols = ("{", "(", "[")
        closing_symbols = ("}", ")", "]")
        last_openings = []
        
        for char in s:
            # if opening, add to queue
            if (char in opening_symbols):
                last_openings.append(char)
                
            # if closing, verify last opening
            if (char in closing_symbols):
                # if no opening, false
                if len(last_openings) == 0:
                    return False
                last_opening = last_openings.pop()
                closing_symbol_index = closing_symbols.index(char)
                
                if char == closing_symbols[closing_symbol_index]:
                    if last_opening != opening_symbols[closing_symbol_index]:
                        return False
        
        # if still openings, false
        if len(last_openings) == 0:
            return True
        
        return False