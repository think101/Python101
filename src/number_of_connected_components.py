from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {num: [] for num in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visit = set()

        def dfs(i):
            if i in visit:
                return 0

            visit.add(i)
            for nei in graph[i]:
                dfs(nei)

            return 1

        res = 0
        for i in range(n):
            res += dfs(i)

        return res


t = Solution()
print(t.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
