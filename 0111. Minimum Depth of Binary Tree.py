from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        que = deque()
        que.append(root)

        res = 0

        while que:
            size = len(que)
            res = res + 1

            for _ in range(size):
                node = que.popleft()
                if not node.left and not node.right:
                    return res

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

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
print(S.minDepth(root))