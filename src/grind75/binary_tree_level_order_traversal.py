from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = []
        q.append(root) if root else None

        while q:
            t = []
            new_q = []
            for i in q:
                t.append(i.val)
                new_q.append(i.left) if i.left else None
                new_q.append(i.right) if i.right else None

            res.append(t)
            q = new_q

        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.levelOrder(root))