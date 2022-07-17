
from platform import freedesktop_os_release


a=[123,2,33]
d=[35.23,97,3]
b=a.sort()
print(a+d)
print(sorted(a+d))


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if len(nums1)%2==1:
            return float(nums1[len(nums1)//2+1])
        else:
            return float((nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2)


def findMedianSortedArrays( nums1: list, nums2: list) -> float:
        nums1[1:1]=nums2
        nums1.sort()
        if len(nums1)%2==1:
            return float(nums1[len(nums1)//2])
        else:
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
print(findMedianSortedArrays(a,d))        
a=Solution()
print(a.findMedianSortedArrays(a,d))
