from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node) -> List[int]:
            if not node:
                return []

            left = inorder(node.left)
            right = inorder(node.right)
            left.append(node.val)
            left.extend(right)

            return left

        io = inorder(root)

        return io[k-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    sol = Solution()
    print(sol.kthSmallest(root, 1))

