from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for p in prerequisites:
            if p[0] not in graph:
                graph[p[0]] = []
            graph[p[0]].append(p[1])

        def dfs(course, visited):
            if course in visited:
                return False
            elif course not in graph or not graph[course]:
                return True

            visited.append(course)
            for p in graph[course]:
                can_finish = dfs(p, visited)
                if not can_finish:
                    return False

                graph[p] = []

            return True

        for i in range(numCourses):
            if not dfs(i, []):
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
    print(sol.canFinish(2, [[1, 0], [0, 1], [0, 2]]))
    print(sol.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
