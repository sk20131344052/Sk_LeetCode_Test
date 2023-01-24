from typing import List

class Solution:
    # 纵向扫描
    def longestCommonPrefix(self, strs:List[str]) -> str:

        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)

        for i in range(length):
            c = strs[0][i]

            for j in range(1, count):
                if i==len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]

        return strs[0]

    # 分治
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start+end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid+1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs)-1)



S = Solution()
strs = ["flower","flow","flight"]
print(S.longestCommonPrefix(strs))
print(S.longestCommonPrefix2(strs))