from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # [a, b] a: max depth, b: max diameter on root
        def depth(root):
            if not root:
                return [-1, -1]

            ld, ldi = depth(root.left)
            rd, rdi = depth(root.right)

            d = max(ld + 1, rd + 1)
            di = max(ld + 1 + rd + 1, ldi, rdi)

            return [d, di]

        return depth(root)[1]


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(s.diameterOfBinaryTree(root))
