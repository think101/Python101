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


t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)

print(Solution().lowestCommonAncestor(t, t.left, t.right).val)
