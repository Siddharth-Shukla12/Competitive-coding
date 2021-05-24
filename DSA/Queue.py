# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:23:07 2021

@author: siddh
"""
from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
q=Queue()
q.enqueue(7)
q.enqueue(8)