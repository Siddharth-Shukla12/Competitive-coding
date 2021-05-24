# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:47:03 2021

@author: siddh
"""
#https://www.codechef.com/TCQL2021/problems/TCQL21C
# cook your dish here
import math
try:
    
    def main():
        fi=list()
        for _ in range(int(input())):
            N,M=list(map(int,input().split()))
            if 0 in (N,M):
                if N==0:
                    fi.append(M)
                else:
                    fi.append(N)
            else:
                g=2*math.gcd(N, M)
                fi.append(g)
        for k in fi:
            print(k)
    main()
except:
    pass