# Definition for a binary tree node.
from typing import  Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def InorderTravel(p):
            if not p:
                return

            InorderTravel(p.left)
            res.append(p.val)
            InorderTravel(p.right)

        InorderTravel(root)

        return res

root = TreeNode(1)
a1 = TreeNode(2)
a2 = TreeNode(3)
root.right = a1
a1.left = a2

S = Solution()
print(S.inorderTraversal(root))

