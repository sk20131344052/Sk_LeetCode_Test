# Definition for a binary tree node.
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(node, target):
            if not node:
                return

            path.append(node.val)
            target -= node.val

            if not node.left and not node.right and target == 0:
                # print(path)
                res.append(path[:])

            dfs(node.left, target)
            dfs(node.right, target)
            path.pop()

        dfs(root, targetSum)
        # print(res)
        # print(path)

        return res




root = TreeNode(5)
a1 = TreeNode(4)
a2 = TreeNode(8)
a3 = TreeNode(11)
a4 = TreeNode(13)
a5 = TreeNode(4)
a6 = TreeNode(7)
a7 = TreeNode(2)
a8 = TreeNode(5)
a9 = TreeNode(1)
root.left = a1
root.right = a2
a1.left = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7
a5.left = a8
a5.right = a9

S = Solution()
print(S.pathSum(root, 22))

