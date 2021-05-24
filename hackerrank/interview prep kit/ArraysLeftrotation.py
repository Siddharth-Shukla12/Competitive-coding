# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:32:31 2021

@author: siddh
"""
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def lefrot(li,b):
    if b>=(len(li)):
        b=b-len(li)
        
    return li[b:]+li[:b]
        
def main():
    a,b=list(map(int,input().rstrip().split()))
    li=list(map(int,input().rstrip().split()))
    for i in lefrot(li, b):
        print(i,end=" ")
main()
    