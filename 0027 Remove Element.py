from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return -1

        n = len(nums)

        slow = -1
        fast = 0

        while fast < n:
            if nums[fast] != val:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow+1

S = Solution()
nums = [3,2,2,3]
val = 3
result = S.removeElement(nums, val)
print(result)