from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph: node -> its prerequisites
        # reverse_graph: node -> nodes which takes the key node as prerequisite
        graph, reverse_graph = {}, {}
        res = []

        for edge in prerequisites:
            if edge[0] not in graph:
                graph[edge[0]] = set()
            if edge[1] not in reverse_graph:
                reverse_graph[edge[1]] = set()

            graph[edge[0]].add(edge[1])
            reverse_graph[edge[1]].add(edge[0])

        queue = []
        for i in range(numCourses):
            if i not in graph:
                queue.append(i)

        while queue:
            for i in range(len(queue)):
                prereq = queue.pop(0)
                res.append(prereq)

                if prereq in reverse_graph:
                    for c in reverse_graph[prereq]:
                        graph[c].remove(prereq)
                        if len(graph[c]) == 0:
                            queue.append(c)

        return res if len(res) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1, 0]]))
    print(sol.findOrder(2, [[1, 0], [0, 1]]))
    print(sol.findOrder(2, [[1, 0], [0, 1], [1, 1]]))
    print(sol.findOrder(2, [[1, 0], [0, 1], [1, 1], [1, 0]]))
    print(sol.findOrder(2, [[1, 0], [0, 1], [1, 1], [1, 0], [0, 0]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [4, 1]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [4, 1], [1, 2]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [4, 1], [1, 2], [2, 3]]))
