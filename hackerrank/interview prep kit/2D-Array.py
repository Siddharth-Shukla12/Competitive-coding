# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:05:19 2021

@author: siddh
"""
#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
if __name__ == '__main__':
    def hourglassSum(arr):
        mat=[]
        for i in range(4):
            for j in range(4):
                mat.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
                
        return max(mat)
    

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))  
