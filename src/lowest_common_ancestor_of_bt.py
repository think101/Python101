from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.findPath(root, p)
        q_path = self.findPath(root, q)

        i = 0
        while True:
            if i == len(p_path) - 1 or i == len(q_path) - 1 or p_path[i + 1].val != q_path[i + 1].val:
                return p_path[i]
            else:
                i += 1

    def findPath(self, root: 'TreeNode', p: 'TreeNode') -> 'List':
        if root is None:
            return None

        if root.val == p.val:
            return [root]

        left = self.findPath(root.left, p)
        if left is not None:
            left.insert(0, root)
            return left

        right = self.findPath(root.right, p)
        if right is not None:
            right.insert(0, root)
            return right

        return None

    def lowestCommonAncestor_TLE(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root

        if self.findNode(root.left, p) and self.findNode(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.findNode(root.right, p) and self.findNode(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def findNode(self, root: 'TreeNode', p: 'TreeNode') -> bool:
        if root is None:
            return False

        if root.val == p.val:
            return True

        return self.findNode(root.left, p) or self.findNode(root.right, p)


t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.left.left = TreeNode(6)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(7)
t.left.right.right = TreeNode(4)
t.right.left = TreeNode(0)
t.right.right = TreeNode(8)

print(Solution().lowestCommonAncestor(t, t.right, t.left.right.right).val)
print(Solution().lowestCommonAncestor_TLE(t, t.right, t.left.right.right).val)
