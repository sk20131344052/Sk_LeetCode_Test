from typing import List

class Solution:
    def generateParenthesis(self, n:int)->List[str]:
        ans = []
        #left:左括号数量   right:右括号数量
        def backtrace(S, left, right):
            if len(S) == 2*n:
                ans.append(''.join(S))
                return
            if left<n:
                S.append('(')
                backtrace(S, left+1, right)
                S.pop()
            if right<left:
                S.append(')')
                backtrace(S, left, right+1)
                S.pop()

        backtrace([], 0, 0)
        return ans

S = Solution()
print(S.generateParenthesis(3))