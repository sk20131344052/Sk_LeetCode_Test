from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = list()
        que = deque()
        que.append(root)

        while que:
            size = len(que)
            level = list()
            for _ in range(size):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(level)
        # return res[::-1]
        res.reverse()
        return res


root = TreeNode(3)
a1 = TreeNode(9)
a2 = TreeNode(20)
a3 = TreeNode(15)
a4 = TreeNode(7)
root.left = a1
root.right = a2
a2.left = a3
a2.right = a4
S = Solution()
print(S.levelOrderBottom(root))