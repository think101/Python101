class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.i = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root:
                return ["N"]

            return [str(root.val)] + preorder(root.left) + preorder(root.right)

        return "_".join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == 'N':
            return None

        self.i = 0
        preorder = data.split("_")

        def helper():
            if self.i >= len(preorder):
                return None
            if preorder[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(preorder[self.i])
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()

    def serialize_TLE(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        res = ""
        q = [root]

        while q:
            if all(x == "n" for x in q):
                break

            for i in range(len(q)):
                node = q.pop(0)
                if node == "n":
                    res += "n_"
                    q.append("n")
                    q.append("n")
                    continue

                res += str(node.val)
                res += "_"

                if node.left:
                    q.append(node.left)
                else:
                    q.append("n")

                if node.right:
                    q.append(node.right)
                else:
                    q.append("n")

            res += "|"

        return res

    def deserialize_TLE(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #print(data)

        if not data:
            return None

        levels = [x for x in data.split("|") if x]

        d = {}  # level index to that level's node list
        for i in range(len(levels)-1, -1, -1):
            nodes = [x for x in levels[i].split("_") if x]
            for j in range(len(nodes)):
                if nodes[j] == "n":
                    nodes[j] = None
                else:
                    nodes[j] = TreeNode(nodes[j])
                    if i != len(levels) - 1:
                        nodes[j].left = d[i+1][j * 2]
                        nodes[j]. right = d[i+1][j * 2 + 1]
            d[i] = nodes

        return d[0][0]


def printBinaryTree(root):
    def preorder(root):
        if not root:
            return []

        return [root.val] + preorder(root.left) + preorder(root.right)

    print(preorder(root))


t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(4)
t.left.left = TreeNode(3)
#print(Codec().serialize(t))
printBinaryTree(Codec().deserialize(Codec().serialize(t)))
