from sqlalchemy import false
class Solution:
    def isValid(self, s: str) -> bool:
        l=list(s)
        if len(l)%2==1: return False
        if len(l)==2:
            if l[0]=='(' and l[1]==')': return True
            if l[0]=='[' and l[1]==']': return True
            if l[0]=='{' and l[1]=='}': return True
            return False
        if l[-1] not in [')','}',']']: return False
        if l[(len(l)//2)-1]=='(' and l[-(len(l)//2)-2] !=')' 
        for i in range(len(l)-1):
            print(i)
            if l[i]=='(':
                if l[-i-1]!=')': 
                    if l[i+1]!=')':
                        return False
            if l[i]=='[' :
                if l[i+1]!=']':
                    if l[-i-1]!=']':
                        return False
            if l[i]=='{' :
                if l[i+1]!='}':
                    if l[-i-1]!='}':
                        return False
        return True
r='{'

s="()[]}{"
l=list(s)
a=Solution()
print(a.isValid(s))