'''
https://www.cnblogs.com/Lin-Yi/p/9600990.html
https://www.jianshu.com/p/8dd18ccb943d?utm_campaign=maleskine&utm_content=note&utm_medium=reader_share&utm_source=weixin
https://blog.csdn.net/zhang_han666/article/details/87980086
'''


'''
这道题需要借助哈希查找key的O(n) 时间复杂度， 否则就会超时

　　 初始化一个 哈希表\字典  dic

头指针start 初始为0

当前指针 cur 初始为0

最大长度变量 l 初始为0

　　用cur变量从给定字符串str的开头开始 一位一位的向右查看字符，直到整个字符串遍历完， 对每一位字符进行如下：

　　　　当前位置的字符为 c = str[cur]

　　　　查询当前字符 c 是否 在哈希表dic的键 当中,表示 当前字符c 是否之前遍历到过

　　　　   如果 当前字符还没出现过，就 在dic中记录一个键值对  (当前字符c，当前位置cur )

　　　　　　cur 后移一位

　　　　   如果 当前字符出现过， 获取 当前字符串c 上次出现的位置 pre = dic[c]

　　　　　　如果pre 在 start后面即 pre>start， 则把start 移动到 pre的下一位， start = pre + 1， 这样保证cur继续向后遍历中 从start到cur没有重复元素

　　　　　　否则 start不动，start移动到某一个位置，说明在这个位置之前有重复的元素了，所以start只往后移动不往回移动

　　　　这时候在衡量一下  如果 cur - start + 1 (衡量当前没重复子串开头到结尾的长度) 比 长度变量 l 大， 那就替换 l 为  cur - start + 1
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        start = 0
        dict = {}
        for i in range(len(s)):
            cur = s[i]
            if cur not in dict:
                dict[cur] = i
            else:
                if dict[cur] + 1 > start:
                    start = dict[cur] + 1
                dict[cur] = i

            l = max(i-start+1, l)

        return l


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("aabaab!bb"))

