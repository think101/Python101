from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { c:set() for c in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].add(prereq)

        res = []
        res_set = set()
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if course in res_set:
                return True

            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            res.append(course)
            res_set.add(course)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(sol.findOrder(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]))
