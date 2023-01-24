from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, MaxPos = len(nums), 0

        for i in range(n):
            if i<= MaxPos:
                MaxPos = max(MaxPos, i+nums[i])
                if MaxPos >= n-1:
                    return True
        return False


S = Solution()
#nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(S.canJump(nums))

