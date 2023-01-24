# Definition for a binary tree node.
from typing import  Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def Valid(p, lower=float('-inf'), upper=float('inf'))->bool:
            if not p:
                return True

            val = p.val
            if val <=lower or val >= upper:
                return False

            if not Valid(p.right, val, upper):
                return False

            if not Valid(p.left, lower, val):
                return False

            return True

        return Valid(root)

root = TreeNode(2)
a1 = TreeNode(1)
a2 = TreeNode(3)
root.left = a1
root.right = a2
S = Solution()
print(S.isValidBST(root))

