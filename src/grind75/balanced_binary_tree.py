from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return [True, 0]

            l = helper(root.left)
            r = helper(root.right)

            if not l[0] or not r[0]:
                return [False, -1]

            return [abs(l[1] - r[1]) <= 1, max(l[1], r[1]) + 1]

        return helper(root)[0]


def isBalanced_ONLGN(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if not root:
                return 0

            return max(depth(root.left), depth(root.right)) + 1

        if not root:
            return True

        l = depth(root.left)
        r = depth(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) \
               and max(l, r) - min(l, r) <= 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)

    s = Solution()
    print(s.isBalanced(root))