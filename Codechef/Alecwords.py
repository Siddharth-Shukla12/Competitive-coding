# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:28:04 2021

@author: siddh
"""
#https://www.codechef.com/JSSC2021/problems/ALECWRDS
try:
    def isSubSequence(string1, string2, m, n):
        if m == 0:
            return True
        if n == 0:
            return False
         
        
        if string1[m-1] == string2[n-1]:
            return isSubSequence(string1, string2, m-1, n-1)
         
    
        return isSubSequence(string1, string2, m, n-1)
    def main():
        fi=[]
        for _ in range(int(input())):
            s1,s2=input().split()
            if isSubSequence(s2, s1, len(s2), len(s1)):
                fi.append('AlecWon')
            else:
                fi.append('AlecLost')
        for k in fi:
            print(k)
    main()
except:
    pass