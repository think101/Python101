from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def helper(node):
            nonlocal res
            if not node:
                return 0

            l, r = max(0, helper(node.left)), max(0, helper(node.right))
            res = max(res, node.val + l + r)

            return max(l, r) + node.val

        helper(root)
        return res


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print(Solution().maxPathSum(t))


#https://stackoverflow.com/questions/11987358/why-nested-functions-can-access-variables-from-outer-functions-but-are-not-allo
