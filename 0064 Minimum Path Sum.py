from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        i, j = 1, 1
        while i < m:
            dp[i][0] = dp[i-1][0] + grid[i][0]
            i += 1
        while j < n:
            dp[0][j] = dp[0][j-1] + grid[0][j]
            j += 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])

        return dp[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
S = Solution()
print(S.minPathSum(grid))