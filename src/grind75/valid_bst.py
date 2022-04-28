from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def isValidBST_wrong(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, left, right):
            if not root:
                return True

            return (left < root.val < right) and isValid(root.left, left, root.val) and isValid(root.right, root.val, right)

        return isValid(root, -float('inf'), float('inf'))


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.isValidBST(root))
