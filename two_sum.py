class Solution:
    def twoSum(self, nums, target: int):
        output=[]
        if nums[0]==nums[1] and nums[0]+nums[1]==target:
                output=[0,1]
                print('1 ret')
                print(output)
                del nums,target
                return output

        for i in nums:

            for j in nums:
                if i==j and i+j==target:# and nums.index(i)!=nums.index(j,nums.index(i)+1):
                    output.append(nums.index(i))
                    try:
                        output.append(nums.index(j,nums.index(i)+1))
                        del j,nums,target
                        break
                    except Exception:
                        output=[]
                    
                
                if i+j==target and nums.index(i)!=nums.index(j):
                    output.append(nums.index(i))
                    output.append(nums.index(j))
                    del j,nums,target
                    break
            
            if len(output)!=0:
                break

        del i
        print(output)
        print('2 ret')
        return output 
a=Solution()
a.twoSum([1,1,1,1,1,1,3,2,2,4],4)
