
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)

        return 2 +  min(self.integerReplacement(n//2), self.integerReplacement(n//2 + 1))


S = Solution()
n = 8
print(S.integerReplacement(n))

