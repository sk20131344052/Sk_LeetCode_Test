from typing import List

# 动态规划
# dp[i][0]表示，到当前位置，以降序结尾的摆动数组的最长子序列的长度
# dp[i][1]表示，到当前位置，以升序结尾的摆动数组的最长子序列的长度
# 所以如果当前是升序的话，则当前位置的升序结尾的最长子序列的长度可以由之前的降序最长子序列的长度加1，此时的降序继续继承前一个状态的长度。
# 若当前是降序同理
# 最终以为我们统计的实际是能追加的个数，需要在结果上再加1表示加上一开始初始的节点个数


# if 升
# {
#     dp[i][降] = dp[i - 1][降]
#     dp[i][升] = dp[i - 1][降] + 1
# }
# if 降
# {
#     dp[i][降] = dp[i - 1][升] + 1
#     dp[i][升] = dp[i - 1][升]
# }


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
            elif nums[i] < nums[i-1]:
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][1] = dp[i-1][0] + 1
                dp[i][0] = dp[i-1][0]

        return max(dp[n-1][0], dp[n-1][1])

S = Solution()
nums = [1,7,4,9,2,5]
nums2 = [1,17,5,10,13,15,10,5,16,8]
print(S.wiggleMaxLength(nums))
print(S.wiggleMaxLength(nums2))













