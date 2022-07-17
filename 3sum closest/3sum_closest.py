class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        l=[]
        c=list(nums)
        c.remove(nums[0])
        print(c)
        v=list(c)
        v.remove(c[0])
        print(v)
        for i in nums:
            for j in  c:
                for k in v:
                    a=i+j+k
                    if a>=target-1:
                        l.append(a)
        print(l)
        # if target in l:
        #     if target+1 in l:
        #         return target+1
        #     return min(l)
        return 0 if len(l)==0 else min(l)



a=Solution()
n=[0,1,2]
t=3
print(a.threeSumClosest(n,t))


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        l=[]
        l2=[]
        for i in range(len(nums)):
            for j in  range(1,len(nums)):
                if i!=j :
                    for k in range(2,len(nums)):
                        if j!=k and i!=k:
                            a=nums[i]+nums[j]+nums[k]
                            if a>=target-1:
                                l.append(a)
                            if a<=target:
                                l2.append(a)
        if len(l)==0 and target>=max(l2): return max(l2) 
        return 0 if len(l)==0 else min(l)



a=Solution()
n=[-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7]
t=255
print(a.threeSumClosest(n,t))