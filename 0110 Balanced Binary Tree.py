# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 自顶向下的递归
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return True
            return max(height(root.left), height(root.right)) + 1

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# 自底向上的递归
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            if left==-1 or right == -1 or abs(left-right)>1:
                return -1
            else:
                return max(left, right) + 1

        return True if height(root)>=0 else False





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
S2 = Solution2()
print(S.isBalanced(root))
print(S2.isBalanced(root))