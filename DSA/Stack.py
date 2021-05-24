# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:12:49 2021

@author: siddh
"""
from collections import deque
class Stack:
    def __init__(self):
        self.s=deque()
    def push(self,n):
        self.s.append(n)
    def pop(self):
        return self.s.pop()
    def peek(self):
        return self.s[-1]
    def is_emp(self):
        return len(self.s)==0
    def size(self):
        return len(self.s)
    def show(self):
        return self.s

def fun(st):
    s1=Stack()
    c=[0,0,0]
    for i in st:
        if i=='(' or i=='{' or i=='[':
            
            s1.push(i)
            if i=='(':
                c[0]+=1
            elif i=='{':
                c[1]+=1
            else:
                c[2]+=1
        elif i==')' or i=='}' or i==']':
            if s1.is_emp():
                return False
            elif i==')':
                c[0]-=1
            elif i=='}':
                c[1]-=1
            else:
                c[2]-=1
            
    if c[0]!=0 or c[1]!=0 or c[2]!=0:
        return False
    elif c[0]==0 and c[1]==0 and c[2]==0:
        return True
    
s=input()
print(fun(s))                
    
