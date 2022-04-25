class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        bfs = [node]
        visited = []
        created = {}

        while bfs:
            t = bfs.pop(0)

            if t.val not in created:
                created[t.val] = Node(t.val, [])
            visited.append(t.val)

            for n in t.neighbors:
                if n.val not in created:
                    created[n.val] = Node(n.val, [])
                    bfs.append(n)

                created[t.val].neighbors.append(created[n.val])

        return created[visited[0]]


if __name__ == '__main__':
    s = Solution()

    n1 = Node(1, [Node(2, [Node(4)]), Node(3, [Node(5)])])
    n2 = s.cloneGraph(n1)
    print(n2.val)
    print(n2.neighbors[0].val)
    print(n2.neighbors[0].neighbors[0].val)
