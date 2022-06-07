from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        index1 = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[index1] + nums[index1-1])/2
        else:
            return nums[index1]


S = Solution()
result = S.findMedianSortedArrays([1,3], [2])
print(result)