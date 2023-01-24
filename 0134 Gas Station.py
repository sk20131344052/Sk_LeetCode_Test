from typing import List

# 暴力求解  不通过
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        j = 0
        remain = 0

        # 总油量 < 总耗油量，一定无解
        if sum(gas) < sum(cost):
            return -1

        for i in range(n):
            j = i
            remain = gas[i]
            # 判断当前剩余的油能否到达下一个点
            while(remain-cost[j]>=0):
                # 减去花费的加上新的点的补给
                remain = remain - cost[j] + gas[(j+1)%n]
                j = (j+1) % n
                # j 回到了 i 即绕了一圈
                if j == i:
                    return i

        # 任何点都不可以
        return -1

S = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(S.canCompleteCircuit(gas, cost))