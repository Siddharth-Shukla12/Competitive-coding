# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:26:06 2021

@author: siddh
"""
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def socks(n,arr):
    sample=list(set(arr))
    a=[]
    for i in range(len(sample)):
        a.append(arr.count(sample[i]))
    s=0
    
    for i in a:
        s+=(i//2)
    return s
def main():
    n=int(input().strip())
    li=list(map(int,input().rstrip().split()))
    print(socks(n,li))
main()
        