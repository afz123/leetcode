class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=list(x)
        j=0
        for i in range(len(l)//2):
            j-=1
            x=(True if l[i]==l[j] else False)
            if x==False:
                return x
        return x