# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:50:03 2021

@author: siddh
"""
from collections import defaultdict
def dfs(start,visited,graph,path):
    path.append(start)
    visited[start]=True
    
    for i in graph[start]:
        if visited[i]==False:
            dfs(i,visited,graph,path)
            
            
    return path
for _ in range(int(input())):
    V,E,L,R=list(input().split())
    V=int(V)
    E=int(E)
    L=int(L)
    R=int(R)
    graph=defaultdict(list)
    for _ in range(E):
        a,b=list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)
    if L<R:
        print(V*L)
    else:
        start=1
        visited=defaultdict(bool)
        path=[]
        t=dfs(start,visited,graph,path)
        if len(t)==V:
            
            print((len(path)-1)*R+L)
        else:
            print(V*L)
        
