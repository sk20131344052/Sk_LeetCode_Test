import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        # freq[c] 表示之后时间里每个字符会出现的次数 初始化为每个字母的频数 遍历过程中减小
        freq = collections.Counter(s)

        for c in s:
            #如果c不在res中, 再考虑是否添加
            if c not in res:
                while len(res)>0 and res[-1]>c and freq[res[-1]]>0:
                    res.pop()
                res.append(c)

            # 无论是否添加c 它之后出现的频数都-1
            freq[c] -= 1

        return ''.join(res)

S = Solution()
s = "bcabc"
print(S.removeDuplicateLetters(s))