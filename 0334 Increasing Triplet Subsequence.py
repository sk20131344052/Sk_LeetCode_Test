from typing import List


#贪心算法  感觉自己肯定想不出来
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False

        first, second = nums[0], float('inf')

        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num

        return False


#双向链表
class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False

        leftMin = [0] * n   # leftMin数组中 leftMin[i]表示 num[0]到nums[i]中的最小值
        leftMin[0] = nums[0]

        rightMax = [0] * n  # rightMax数组中 rightMax[i]表示 num[i]到nums[n-1]中的最大值
        rightMax[n-1] = nums[n-1]

        for i in range(1, n):
            leftMin[i] = min(leftMin[i-1], nums[i])

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], nums[i])

        for i in range(1, n-1):
            if leftMin[i-1] < nums[i] < rightMax[i+1]:
                return True
        return False


nums = [1, 2, 3, 4, 5]
S = Solution()
S2 = Solution2()
print(S.increasingTriplet(nums))
print(S2.increasingTriplet(nums))