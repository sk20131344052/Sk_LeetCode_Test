# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        preorderList = []

        def preorderTraversal(root: TreeNode):
            if not root:
                return
            preorderList.append(root)
            preorderTraversal(root.left)
            preorderTraversal(root.right)

        preorderTraversal(root)
        n = len(preorderList)
        for i in range(1, n):
            pre, cur = preorderList[i-1], preorderList[i]
            pre.left = None
            pre.right = cur

        return root

