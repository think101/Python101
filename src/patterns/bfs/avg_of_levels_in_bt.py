from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        q.append(root)

        res = []

        while (q):
            sum = 0
            cnt = len(q)

            for i in range(cnt):
                n = q.pop(0)
                sum += n.val

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            res.append(sum / cnt)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.averageOfLevels(TreeNode(1, TreeNode(2), TreeNode(3))))

