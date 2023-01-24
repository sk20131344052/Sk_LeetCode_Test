# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, res):
            if not root:
                return None

            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

            return res

        def findTwoSwapped(nums, swapper):
            index = -1
            index2 = -1
            indexs = []

            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    indexs.append(i)

            # 这种情况是相邻的结点有问题
            if len(indexs) == 1:
                swapper.append(nums[indexs[0]])
                swapper.append(nums[indexs[0]+1])
            elif len(indexs) == 2:
                swapper.append(nums[indexs[0]])
                swapper.append(nums[indexs[1]+1])

            return swapper

        def recover(root, count, x, y):
            if not root:
                return
            if count<=0:
                return

            if root.val == x:
                root.val = y
                count -= 1
            elif root.val == y:
                root.val = x
                count -= 1

            recover(root.left, count, x, y)
            recover(root.right, count, x, y)


        nums = inorder(root, [])
        # print(nums)
        swapper = findTwoSwapped(nums, [])
        # print(swapper)
        recover(root, 2, swapper[0], swapper[1])
        nums2 = inorder(root, [])
        # print(nums2)



root = TreeNode(1)
a1 = TreeNode(3)
a2 = TreeNode(2)
root.left = a1
a1.right = a2


S = Solution()
S.recoverTree(root)