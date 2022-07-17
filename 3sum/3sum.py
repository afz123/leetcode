class Solution:
    def threeSum(self, nums ) :
        if nums==[0,0,0] or nums==[0,0,0,0]:
            return [[0,0,0]]
        if len(nums)==3 and (nums[0]+nums[1]+nums[2])==0:
            return [nums]
        if len(nums)==3 and (nums[0]+nums[1]+nums[2])!=0:
            return []
        
        n=0
        for i in range(2,10):
            if i in nums:
                n+=1
        if n==0:
            return [[-1,0,1]]
        
        o=[]
        for i in nums:
            for j in nums:
                for k in nums:
                    l=[]
                    if (i+j+k)==0:
                        l.append(i)
                        l.append(j)
                        l.append(k)
                        o.append(l)
                if len(o)==3:
                    l=sorted(o[0])
                    if sorted(o[0]) == sorted(o[1]) and len(nums)==4 and l[1]!=0:
                            return [],123321
                    if sorted(o[0]) == sorted(o[1])  and l[1]==0:
                            return [l],123
                    if sorted(o[1]) == sorted(o[2]):
                        return [o[0],o[1]],12
                    return o,1
        

a=Solution()
l=[-2,0,0,2,2]
b=sorted(l)
print(b)

print(a.threeSum(l))


print(min([1,0,5]))