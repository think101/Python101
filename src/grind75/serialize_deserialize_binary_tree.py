class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def inorder(root):
            if not root:
                return "n"

            return inorder(root.left) + "_" + str(root.val) + "_" + inorder(root.right)

        def preorder(root):
            if not root:
                return "n"

            return str(root.val) + "_" + preorder(root.left) + "_" + preorder(root.right)

        return preorder(root) + "|" + inorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)

        i = data.index('|')
        preorder = data[0:i]
        inorder = data[i + 1:]

        p = [x for x in preorder.split('_') if x]
        i = [x for x in inorder.split('_') if x]

        def construct_tree(p_order, i_order):
            if not p_order or len(p_order) == 1 and p_order[0] == "n":
                return None

            index = i_order.index(p_order[0])
            p_left = p_order[1:index + 1]
            p_right = p_order[index + 1:]

            i_left = i_order[0:index]
            i_right = i_order[index + 1:]

            res = TreeNode(p_order[0])
            res.left = construct_tree(p_left, i_left)
            res.right = construct_tree(p_right, i_right)
            return res

        return construct_tree(p, i)


t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(4)
t.left.left = TreeNode(3)
#print(Codec().serialize(t))
print(Codec().deserialize(Codec().serialize(t)))
