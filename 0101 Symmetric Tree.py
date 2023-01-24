from typing import  Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        p, q = root.left, root.right

        def dfs(p, q):
            if not p and not q:
                return True
            if (not p or not q) or p.val != q.val:
                return False

            return dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(p, q)

#改造为迭代
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        p, q = root.left, root.right

        def check(p, q):
            queue1 = collections.deque()
            queue1.append(p)
            queue1.append(q)

            while queue1:
                node1 = queue1.popleft()
                node2 = queue1.popleft()

                if not node1 and not node2:
                    continue
                if (not node1 or not node2) or node1.val != node2.val:
                    return False

                queue1.append(node1.left)
                queue1.append(node2.right)
                queue1.append(node1.right)
                queue1.append(node2.left)
            return True

        return check(p, q)



root = TreeNode(1)
a1 = TreeNode(2)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(4)
a6 = TreeNode(3)
root.left = a1
root.right = a2
a1.left = a3
a1.right = a4
a2.left = a5
a2.right = a6

S = Solution()
print(S.isSymmetric(root))

S2 = Solution2()
print(S2.isSymmetric(root))





