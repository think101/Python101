from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = float('-inf')


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res = float('-inf')

        def helper(node: Optional[TreeNode]) -> int:
            global res

            if not node:
                return float('-inf')

            l, r = max(0, helper(node.left)), max(0, helper(node.right))
            res = max(res, node.val + l + r)

            return max(l, r) + node.val

        helper(root)

        return res


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print(Solution().maxPathSum(t))
