from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        q = [root]

        while q:
            res += 1
            for i in range(len(q)):
                tn = q.pop(0)
                if not tn.left and not tn.right:
                    return res

                if tn.left:
                    q.append(tn.left)
                if tn.right:
                    q.append(tn.right)

        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    s = Solution()
    print(s.minDepth(root))
