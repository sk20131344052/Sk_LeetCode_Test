from typing import List
from collections import deque
from typing import  Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        que = deque()

        high = 0

        que.append(root)

        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            high += 1

        return high


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
print(S.maxDepth(root))