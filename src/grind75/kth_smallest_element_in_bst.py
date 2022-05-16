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

    def kthSmallest_count(self, root: Optional[TreeNode], k: int) -> int:

        def count(root):
            if not root:
                return 0
            return count(root.left) + 1 + count(root.right)

        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    print(Solution().kthSmallest(root, 1))
    print(Solution().kthSmallest_count(root, 1))
    print(Solution().kthSmallest(root, 2))
    print(Solution().kthSmallest_count(root, 2))
