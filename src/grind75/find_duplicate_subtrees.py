from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False

            return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

        def addAll(root):
            if not root:
                return

            result.append(root)
            addAll(root.left)
            addAll(root.right)

        def helper(root1, root2):
            if not root1 or not root2:
                return

            if sameTree(root1, root2):
                addAll(root1)
            else:
                helper(root1, root2.left)
                helper(root1, root2.right)
                helper(root1.left, root2)
                helper(root1.right, root2)

        helper(root.left, root.right)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)

    solution = Solution()
    print(solution.findDuplicateSubtrees(root))
