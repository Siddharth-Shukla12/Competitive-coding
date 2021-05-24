# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:39:58 2021

@author: siddh
"""
#https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a,b,k=query[0]-1,query[1],query[2]
        array[a] += k
        array[b] -= k
        
    m = 0
    r = 0
    for i in array:
        r += i
        if r > m:
            m = r
            
    return m
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)