from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node.val] + inorder(node.right)

        return inorder(root)[k-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    print(Solution().kthSmallest(root, 1))
    print(Solution().kthSmallest(root, 2))
