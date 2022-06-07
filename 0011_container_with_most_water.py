from typing import List


class Solution:
    #双指针
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while True:
            if left == right:
                break
            cur_area = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            max_area = max(cur_area, max_area)
        return max_area


S = Solution()
result = S.maxArea([1,8,6,2,5,4,8,3,7])
print(result)

