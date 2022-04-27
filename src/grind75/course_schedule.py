from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = []
        for p in prerequisites:
            if p[0] not in adj:
                adj[p[0]] = []
            adj[p[0]].append(p[1])

        def dfs(n, visiting):
            if n not in adj or n in visited:
                return True

            visiting.append(n)

            for i in adj[n]:
                if i in visiting:
                    return False
                if not dfs(i, visiting):
                    return False
            visiting.pop(len(visiting) - 1)
            visited.append(n)
            return True

        for i in range(numCourses):
            visiting = []
            if not dfs(i, visiting):
                return False

        return True

t = Solution()
print(t.canFinish(2, [[1, 0]]))
print(t.canFinish(2, [[1, 0], [0, 1]]))
