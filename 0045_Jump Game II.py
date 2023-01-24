from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0

        for i in range(n-1):
            if i<= maxPos:
                maxPos = max(maxPos, i+nums[i])

                if maxPos >= n-1:
                    return step+1

                if i == end:
                    end = maxPos
                    step += 1

        return step


S = Solution()
nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
print(S.jump(nums))

