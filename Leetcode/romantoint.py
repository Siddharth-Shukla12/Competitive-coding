#https://leetcode.com/problems/roman-to-integer/submissions/
def romanToInt(s) :
        d=dict()
        n=len(s)
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':500,'CM':900}   
        su=0
        k=0
        while k <n:
            if k!=(n-1):
                if s[k]=='I' and s[k+1]=='V':
                    su+=4
                    k=k+2
                elif s[k]=='I' and s[k+1]=='X':
                    su+=9
                    k=k+2
                elif s[k]=='X' and s[k+1]=='L':
                    su+=40
                    k=k+2
                elif s[k]=='X' and s[k+1]=='C':
                    su+=90
                    k=k+2
                elif s[k]=='C' and s[k+1]=='D':
                    su+=400
                    k=k+2
                elif s[k]=='C' and s[k+1]=='M':
                    su+=900
                    k=k+2
                else:
                    su+=d[s[k]]
                    k+=1
            else:
                su+=d[s[k]]
                k+=1
        return su
s=input()
print(romanToInt(s))