from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}    # course to its prereqs
        r_graph = {}  # course to courses which takes it as prereq

        for pre in prerequisites:
            graph.setdefault(pre[0], set()).add(pre[1])
            r_graph.setdefault(pre[1], set()).add(pre[0])

        q = []
        for i in range(numCourses):
            if i not in graph:
                q.append(i)

        while q:
            c = q.pop(0)

            delete = []
            if c in r_graph:
                for course in r_graph[c]:
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
