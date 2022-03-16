"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        created = {}
        visited = []
        bfs = [node]



        while bfs:
            n = bfs.pop(0)
            visited.append(n.val)
            if n.val not in created:
                created[n.val] = Node(n.val, [])

            new_node = created[n.val]

            for neighbor in n.neighbors:
                if neighbor.val not in visited and neighbor.val not in created:
                    bfs.append(neighbor)

                if neighbor.val not in created:
                    created[neighbor.val] = Node(neighbor.val, [])

                new_node.neighbors.append(created[neighbor.val])

        return created[1]

