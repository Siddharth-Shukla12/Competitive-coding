# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:34:55 2021

@author: siddh
"""
#https://www.codechef.com/START5B/problems/SLPCYCLE
for _ in range(int(input())):
    L,H=list(map(int,input().split()))
    s=input()
    li=[len(i) for i in s.split('1') if i!='']
    j=0
    s1='0'*H
    if s1 in s:
	    print('YES')
	    continue
    while j!=len(li) and H>0:
        H=2*(H-li[j])
        
        j+=1
    if H<=0:
        print('YES')
    else:
        print('NO')