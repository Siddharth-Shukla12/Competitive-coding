# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:51:47 2021

@author: siddh
"""
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumSwaps(arr):
    c=0
    for i in range(len(arr)):
        
        while arr[i]!=(i+1):
            t=arr[i]-1
            arr[i],arr[t]=arr[t],arr[i]
            c+=1
    return c
def main():
    n=int(input())
    li=list(map(int,input().rstrip().split()))
    if len(li)==n:
        print(minimumSwaps(li))
main()