from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res = float('-inf')

        def helper(root: Optional[TreeNode]) -> int:
            global res

            if not root:
                return float('-inf')

            l, r = max(0, helper(root.left)), max(0, helper(root.right))
            res = max(res, root.val + l + r)

            return max(l, r) + root.val

        helper(root)

        return res
