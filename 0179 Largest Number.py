import  functools
from typing import  List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)       #将数字映射成为字符

        def cmp(a, b):
            if a+b == b+a:
                return 0
            elif a+b > b+a:
                return 1
            else:
                return -1

        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'

S = Solution()
nums = [10,2]
print(S.largestNumber(nums))

