from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        q = [root]

        while q:
            level = []
            for i in range(len(q)):
                t = q.pop(0)
                if not t:
                    continue
                level.append(t.val)
                q.append(t.left)
                q.append(t.right)

            levels.append(level)

        res = []
        for l in levels:
            if l:
                res.append(l[-1])

        return res
