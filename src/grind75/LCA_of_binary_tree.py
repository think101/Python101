class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(root):
            if not root:
                return [False, None]

            left = helper(root.left)
            right = helper(root.right)

            if left[1]:
                return left

            if right[1]:
                return right

            if root.val == p.val or root.val == q.val:
                if left[0] or right[0]:
                    return [True, root]
                else:
                    return [True, None]

            if left[0] and right[0]:
                return [True, root]

            return [left[0] or right[0], None]

        return helper(root)[1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(4)

    p = root.left.left
    q = root.right.right
    solution = Solution()
    print(solution.lowestCommonAncestor(root, p, q).val)
