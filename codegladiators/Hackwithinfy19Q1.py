#Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish. He wants to choose as many dishes as possible from the given list but while satisfying two conditions:

# He can choose only one type of dish.
# No two chosen dishes should be adjacent to each other.
# Ramu wants to know which type of dish he should choose from, so that he can pick the maximum number of dishes.

# Example :

# Given N= 9 and A= [1,2,2,1,2,1,1,1,1]

# For type 1, Ramu can choose at most four dishes. One of the ways to choose four dishes of type 1 is A1,A4, A7 and A9.

# For type 2, Ramu can choose at most two dishes. One way is to choose A3 and A5.

# So in this case, Ramu should go for type 1, in which he can pick more dishes.

# INPUT FORMAT:

# The first line contains T, the number of test cases. Then the test cases follow.
# For each test case, the first line contains a single integer N.
# The second line contains N integers A1,A2,…,AN.
# OUTPUT FORMAT

# For each test case, print a single line containing one integer ― the type of the dish that Ramu should choose from. If there are multiple answers, print the smallest one.

# CONSTRAINTS :

# 1 <= T <= 10^3
# 1 <= N <= 10^3
# 1 <= Ai <= 10^3
def fin(li):
    c=1
    a=[]
    t=[]
    for i in range(len(li)-1):
        if li[i+1]==li[i]:
            
            c+=1
        else:
           a.append((c,li[i]))
           c=1
    if li[-1]==li[len(li)-2]:
        a.append((c,li[i]))
        c=1
    else:
        a.append((c,li[-1]))
    for (b,c) in a:
        if b%2!=0:
            for j in range((b//2)+1):
                t.append(c)
        else:
            for j in range((b//2)):
                t.append(c)
    return t
def main():
    fi=[]
    for i in range(int(input())):
        n=int(input())
        li=list(map(int,input().split()))
        l=fin(li)
        l.sort()
        x=[]
        for j in l:
            x.append(l.count(j)) 
        k=max(x)
        for j in l:
            if l.count(j)==k:
                fi.append(j)
                break
    for m in fi:
        print(m)
main()
            
            