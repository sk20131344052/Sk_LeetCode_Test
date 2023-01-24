from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]


        for i in range(len(nums)):
            pre = max(pre+nums[i], nums[i])
            maxAns = max(pre, maxAns)

        return maxAns

S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(S.maxSubArray(nums))