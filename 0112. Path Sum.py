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

    # 递归
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            else:
                return False

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

    # 广度搜索
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        que = deque()
        que.append(root)
        que2 = deque()
        que2.append(root.val)

        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                sum  = que2.popleft()

                if not node.left and not node.right:
                    if sum == targetSum:
                        return True

                if node.left:
                    que.append(node.left)
                    que2.append(sum+node.left.val)

                if node.right:
                    que.append(node.right)
                    que2.append(sum + node.right.val)
        return False



root = TreeNode(1)
a1 = TreeNode(2)
a2 = TreeNode(3)
root.left = a1
root.right = a2

S = Solution()
print(S.hasPathSum(root, 3))

S = Solution()
print(S.hasPathSum2(root, 5))