from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        i = inorder.index(preorder[0])
        return TreeNode(preorder[0], self.buildTree(preorder[1:i + 1], inorder[0:i]),
                        self.buildTree(preorder[i + 1:], inorder[i + 1:]))


if __name__ == "__main__":

    def print_tree(root: Optional[TreeNode]):
        if not root:
            return
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


    s = Solution()
    print_tree(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
