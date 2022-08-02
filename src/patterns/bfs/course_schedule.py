from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for pre in prerequisites:
            graph.setdefault(pre[0], set()).add(pre[1])

        q = []
        for i in range(numCourses):
            if i not in graph:
                q.append(i)

        while q:
            c = q.pop(0)

            delete = []
            for course in graph:
                if c in graph[course]:
                    graph[course].remove(c)
                if len(graph[course]) == 0:
                    delete.append(course)
                    q.append(course)

            [graph.pop(key) for key in delete]

        if len(graph):
            return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
