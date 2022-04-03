from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        current_level = [root]
        current_res = []
        next_level = []

        while True:
            for i in range(len(current_level)):
                n = current_level[i]
                current_res.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            res.append(current_res)

            if next_level:
                current_level = next_level
                next_level = []
                current_res = []
            else:
                break

        return res


t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().levelOrder(t))
t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(Solution().levelOrder(t))

