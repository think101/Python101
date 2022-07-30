class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        origToCopy = {}

        def dfs(n):
            if n in origToCopy:
                return origToCopy[n]

            copy = Node(n.val)
            origToCopy[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else node


if __name__ == "__main__":
    node = Node(1, [Node(2, [Node(3)]), Node(4)])
    sol = Solution()
    print(sol.cloneGraph(node))
