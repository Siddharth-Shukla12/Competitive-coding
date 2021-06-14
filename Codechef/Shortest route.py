# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:16:57 2021

@author: siddh
"""
try:
    for _ in range(int(input())):
            N,M=list(map(int,input().split()))
            T=list(map(int,input().split()))
            D=list(map(int,input().split()))
            l1=[]
            l2=[]
            if T[0]==1:
                l1.append(0)
            else:
                l1.append(None)
            
            for i in range(1,N):
                if T[i]==1:
                    l1.append(0)
                elif l1[-1] is not None:
                    l1.append(l1[-1]+1)
                else:
                    l1.append(None)
        
            if T[-1]==2:
                l2.append(0)
            else:
                l2.append(None)
            for i in range(N-2,-1,-1):
                if T[i]==2:
                    l2.append(0)
                elif l2[-1] is not None:
                    l2.append(l2[-1]+1)
                else:
                    l2.append(None)
            
            l2=l2[::-1]
            for i in D:
                if (i-1)==0:
                    print(0,end=' ')
                    continue
                if l1[i-1] is None and l2[i-1] is None:
                    print(-1,end=' ')
                elif l1[i-1] is None and l2[i-1] is not None:
                    print(l2[i-1],end=' ')
                elif l1[i-1] is not None and l2[i-1] is None:
                    print(l1[i-1],end=' ')
                else:
                    print(min(l1[i-1],l2[i-1]),end=' ')
                
                    
                
                
            print()
except:
    pass
        