class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        for i,j in enumerate(sorted(nums)): 
            if j==val: nums.remove(j)
        return len(nums)