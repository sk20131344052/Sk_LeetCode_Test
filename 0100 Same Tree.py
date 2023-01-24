import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False

            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


p = TreeNode(1)
q = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(2)
e = TreeNode(3)

p.left = b
p.right = c
q.left = d
q.right = e


S = Solution()
print(S.isSameTree(p, q))

S2 = Solution2()
print(S2.isSameTree(p, q))