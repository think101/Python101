from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(r1, r2):
            if not r1 and not r2:
                return True

            if (r1 and not r2) or (not r1 and r2) or (r1.val != r2.val):
                return False

            return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)

        if not root:
            return False

        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


t = TreeNode(3, TreeNode(5), TreeNode(4, TreeNode(1), TreeNode(2)))
s = TreeNode(4, TreeNode(1), TreeNode(2))
print(Solution().isSubtree(t, s))

