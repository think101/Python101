from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, a, b):
            if not node:
                return True

            if a < node.val < b:
                return helper(node.left, a, node.val) and helper(node.right, node.val, b)

            return False

        return helper(root, float(-inf), float(inf))


