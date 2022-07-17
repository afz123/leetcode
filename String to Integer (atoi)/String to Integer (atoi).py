import regex as re
class Solution:
    def myAtoi(self, s: str) -> int:
    pattern = '\s*([\+,\-])?[0]*([0-9]*).*'
    x = re.search(pattern,s).groups()[:2]
    val = eval(x[1]) if x[1] else 0
    sign = -1 if x[0]=='-' else 1
    return max(-2**31, min(2**31-1, sign*val))


class Solution:
    def myAtoi(self, s: str) -> int:
        l=list(s)
        lc=['-','0','1','2','3','4','5','6','7','8','9']
        output=[]
        for i in l:
            if i in lc:
                output.append(i)
        return int(''.join(output)) if int(''.join(output))<2147483646 and int(''.join(output))>-2147483646 else 0