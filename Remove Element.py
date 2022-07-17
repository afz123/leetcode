class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i,j in enumerate(sorted(nums)): 
            if j==val: nums.remove(j)
        return len(nums)