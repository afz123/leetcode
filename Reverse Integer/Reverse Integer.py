'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        l=list(str(x))
        if l[-1]=='0':
            del l[-1]
        l.reverse()
        if l[-1]=='-':
            del l[-1]
            l.insert(0,'-')
        return int(''.join(l)) if int(''.join(l))<2147483646 and int(''.join(l))>-2147483646 else 0