from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)

        i = inorder.index(preorder[0])
        inorder_l = inorder[:i]
        inorder_r = inorder[i+1:]

        preorder_l = preorder[1:1+i]
        preorder_r = preorder[1+i:]

        return TreeNode(preorder[0], self.buildTree(preorder_l, inorder_l),
                        self.buildTree(preorder_r, inorder_r))

