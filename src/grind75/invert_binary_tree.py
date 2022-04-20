from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        t = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = t

        return root


def print_tree(root: Optional[TreeNode]):
    if not root:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
s = Solution()
print_tree(s.invertTree(t))
