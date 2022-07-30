class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        origToCopy = {}
        q = []

        q.append(node)

        while (q):
            cnt = len(q)
            for i in range(cnt):
                n = q.pop(0)

                if n not in origToCopy:
                    origToCopy[n] = Node(n.val)

                c = origToCopy[n]
                for neighbor in n.neighbors:
                    if neighbor in origToCopy:
                        c.neighbors.append(origToCopy[neighbor])
                        continue

                    q.append(neighbor)
                    neighborCopy = Node(neighbor.val)
                    origToCopy[neighbor] = neighborCopy
                    c.neighbors.append(neighborCopy)

        return origToCopy[node]
